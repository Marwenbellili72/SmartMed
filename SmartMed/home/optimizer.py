import numpy as np
import math
import random

class CTScannerOptimization:
    def __init__(self, lower_bounds, upper_bounds):

        if len(lower_bounds) != 3 or len(upper_bounds) != 3:
            raise ValueError("Les bornes doivent contenir exactement 3 valeurs [mA, time, rpm]")
        if any(l >= u for l, u in zip(lower_bounds, upper_bounds)):
            raise ValueError("Les bornes supérieures doivent être strictement supérieures aux bornes inférieures")
        if any(l <= 0 for l in lower_bounds):
            raise ValueError("Toutes les bornes inférieures doivent être strictement positives")
            
        self.num_generations = 50
        self.pop_size = 50
        self.num_genes = 3  
        
        self.lower_bounds = np.array(lower_bounds)
        self.upper_bounds = np.array(upper_bounds)
        
        self.population = self._initialize_population()
    
    def _initialize_population(self):
        return np.random.uniform(
            low=self.lower_bounds,
            high=self.upper_bounds,
            size=(self.pop_size, self.num_genes)
        )
    
    def calculate_objectives(self, solution):
        mA, time, rpm = solution
        if rpm <= 0:
            raise ValueError("RPM doit être strictement positif")
        dose = mA * time / rpm
        quality = (mA * time) / np.log(rpm + 1)
        return dose, quality
    
    def _dominates(self, obj1, obj2):
        return (obj1[0] <= obj2[0] and obj1[1] <= obj2[1]) and (obj1[0] < obj2[0] or obj1[1] < obj2[1])
    
    def _non_dominated_sort(self, population):
        pop_size = len(population)
        S = [[] for _ in range(pop_size)]
        front = [[]]
        n = np.zeros(pop_size)
        rank = np.zeros(pop_size)
        
        for p in range(pop_size):
            obj_p = self.calculate_objectives(population[p])
            for q in range(pop_size):
                obj_q = self.calculate_objectives(population[q])
                
                if self._dominates(obj_p, obj_q):
                    S[p].append(q)
                elif self._dominates(obj_q, obj_p):
                    n[p] += 1
            
            if n[p] == 0:
                rank[p] = 0
                front[0].append(p)
        
        i = 0
        while front[i]:
            next_front = []
            for p in front[i]:
                for q in S[p]:
                    n[q] -= 1
                    if n[q] == 0:
                        rank[q] = i + 1
                        next_front.append(q)
            i += 1
            if next_front:
                front.append(next_front)
            if i >= len(front):  
                break
        return front
    
    def _crowding_distance(self, front, objectives):
        distances = np.zeros(len(front))
        if len(front) <= 2:
            distances[:] = np.inf
            return distances
        
        for obj_idx in range(2):  
            sorted_idx = np.argsort([objectives[i][obj_idx] for i in front])
            distances[sorted_idx[0]] = distances[sorted_idx[-1]] = np.inf
            
            obj_range = objectives[front[sorted_idx[-1]]][obj_idx] - objectives[front[sorted_idx[0]]][obj_idx]
            if obj_range == 0:
                continue
                
            for i in range(1, len(front) - 1):
                distances[sorted_idx[i]] += (
                    objectives[front[sorted_idx[i + 1]]][obj_idx] -
                    objectives[front[sorted_idx[i - 1]]][obj_idx]
                ) / obj_range
        
        return distances
    
    def _crossover(self, parent1, parent2):
        child = np.zeros_like(parent1)
        for i in range(len(parent1)):
            beta = random.random()
            child[i] = beta * parent1[i] + (1 - beta) * parent2[i]
        return np.clip(child, self.lower_bounds, self.upper_bounds)
    
    def _mutation(self, solution):
        mutated = solution.copy()
        for i in range(len(mutated)):
            if random.random() < 0.1:  
                delta = (random.random() - 0.5) * 0.1  
                mutated[i] *= (1 + delta)
        return np.clip(mutated, self.lower_bounds, self.upper_bounds)
    
    def run_optimization(self, max_generations=None):
        if max_generations is None:
            max_generations = self.num_generations
        else:
            max_generations = max(1, int(max_generations))
            
        population = self.population
        
        for gen in range(max_generations):
            offspring = np.zeros((self.pop_size, self.num_genes))
            for i in range(0, self.pop_size, 2):
                p1, p2 = random.sample(range(self.pop_size), 2)
                offspring[i] = self._mutation(self._crossover(population[p1], population[p2]))
                offspring[i+1] = self._mutation(self._crossover(population[p2], population[p1]))
            
            combined_pop = np.vstack((population, offspring))
            
            objectives = [self.calculate_objectives(sol) for sol in combined_pop]
            
            fronts = self._non_dominated_sort(combined_pop)
            
            new_pop = []
            front_idx = 0
            
            while front_idx < len(fronts) and len(new_pop) + len(fronts[front_idx]) <= self.pop_size:
                new_pop.extend(fronts[front_idx])
                front_idx += 1
            
            if len(new_pop) < self.pop_size and front_idx < len(fronts):
                last_front = fronts[front_idx]
                distances = self._crowding_distance(last_front, objectives)
                sorted_indices = np.argsort(distances)[::-1]
                
                remaining = self.pop_size - len(new_pop)
                new_pop.extend([last_front[i] for i in sorted_indices[:remaining]])
            
            population = combined_pop[new_pop]
            
            if gen % 10 == 0:
                print(f"Génération {gen}: Taille du front de Pareto = {len(fronts[0])}")
        
        if fronts: 
            final_front = fronts[0]
            result = self.get_best_solution([combined_pop[i] for i in final_front], preference="weighted")
            return result
        else:
            return None
    
    def get_best_solution(self, pareto_front, preference="weighted"):
        
        if not len(pareto_front):
            return None
            
        if preference not in ["min_dose", "max_quality", "weighted"]:
            raise ValueError("Préférence invalide. Utiliser 'min_dose', 'max_quality' ou 'weighted'")
        
        best_fitness = float('inf')
        result = None
        
        for solution in pareto_front:
            if len(solution) != 3:
                raise ValueError("Chaque solution dans le front de Pareto doit contenir exactement 3 valeurs [mA, time, rpm]")
            
            mA, time, rpm = solution
            dose, quality = self.calculate_objectives(solution)
            
            if preference == "min_dose":
                fitness = dose
            elif preference == "max_quality":
                fitness = -quality  
            else:  
                fitness = dose - quality
            
            if fitness < best_fitness:
                best_fitness = fitness
                result = {
                    "mA": float(mA),
                    "time": float(time),
                    "rpm": float(rpm),
                    "dose": float(dose),
                    "quality": float(quality),
                    "fitness": float(fitness)
                }
        
        return result