import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image

# ==========================================
# 1. HYPERPARAMETERS
# ==========================================
POPULATION_SIZE = 100    # Number of images in each generation
GENERATIONS = 1000       # How many generations to run
MUTATION_RATE = 0.05     # Probability of a pixel mutating (5%)
IMAGE_SIZE = (32, 32)    # Downscale image to 32x32 for faster computation

# ==========================================
# 2. HELPER FUNCTIONS
# ==========================================
def load_and_preprocess_image(image_path):
    """Loads the target image, resizes it, and converts it to a NumPy array."""
    try:
        img = Image.open(image_path)
        img = img.convert("RGB") # Ensure it has RGB channels (no transparency)
        img = img.resize(IMAGE_SIZE)
        return np.array(img)
    except Exception as e:
        print(f"Warning: Could not load '{image_path}'.")
        print("Creating a default target pattern (a colored square) instead.")
        # Create a simple default target if no image is found
        img = np.zeros((IMAGE_SIZE[0], IMAGE_SIZE[1], 3), dtype=np.uint8)
        img[8:24, 8:24] = [255, 100, 50] # Draw a square
        return img

def calculate_fitness(individual, target):
    """
    Calculates fitness based on Mean Squared Error (MSE).
    Lower MSE means the image is closer to the target.
    We return negative MSE so that a HIGHER value means BETTER fitness.
    """
    mse = np.mean((individual.astype("float") - target.astype("float")) ** 2)
    return -mse

def initialize_population(size, shape):
    """Creates the initial population of random noise images."""
    return [np.random.randint(0, 256, shape, dtype=np.uint8) for _ in range(size)]

def crossover(parent1, parent2):
    """Uniform crossover: randomly selects pixels from either parent1 or parent2."""
    # Create a random boolean mask (True or False)
    mask = np.random.rand(*parent1.shape) > 0.5
    # Where mask is True, take parent1's pixel; otherwise, take parent2's pixel
    child = np.where(mask, parent1, parent2)
    return child

def mutate(individual, mutation_rate):
    """Randomly mutates some pixels in the image to brand new random colors."""
    # Create a boolean mask deciding which pixels will mutate
    mask = np.random.rand(*individual.shape) < mutation_rate
    # Generate random colored pixels for the entire image
    random_pixels = np.random.randint(0, 256, individual.shape, dtype=np.uint8)
    # Replace old pixels with random pixels where the mask is True
    mutated = np.where(mask, random_pixels, individual)
    return mutated

# ==========================================
# 3. MAIN GENETIC ALGORITHM
# ==========================================
def main():
    print("Loading target image...")
    # Load the target image (Make sure you have an image named 'target.jpg' in the folder)
    target_image = load_and_preprocess_image("target.jpg")
    img_shape = target_image.shape
    
    print(f"Initializing population of {POPULATION_SIZE} random images...")
    population = initialize_population(POPULATION_SIZE, img_shape)
    
    best_individual = None
    
    print("Starting Evolution...")
    # The Evolution Loop
    for generation in range(GENERATIONS):
        # 1. Evaluate fitness for all individuals in the current population
        fitness_scores = [calculate_fitness(ind, target_image) for ind in population]
        
        # 2. Sort the population by fitness in descending order (highest fitness first)
        sorted_indices = np.argsort(fitness_scores)[::-1]
        population = [population[i] for i in sorted_indices]
        
        best_fitness = fitness_scores[sorted_indices[0]]
        best_individual = population[0]
        
        # Print progress every 100 generations
        if (generation + 1) % 100 == 0:
            print(f"Generation {generation + 1}/{GENERATIONS} | Best Fitness (Negative MSE): {best_fitness:.2f}")
            
        # 3. Selection (Elitism)
        # Take the top 20% of the population to act as parents for the next generation
        num_parents = int(POPULATION_SIZE * 0.2)
        parents = population[:num_parents]
        
        # 4. Create the next generation
        new_population = []
        
        # Keep the absolute best individual unchanged (Strict Elitism)
        new_population.append(parents[0])
        
        # Breed the rest to fill up the population size
        while len(new_population) < POPULATION_SIZE:
            # Randomly select two parents from the top 20% pool
            p1 = random.choice(parents)
            p2 = random.choice(parents)
            
            # Perform crossover and mutation
            child = crossover(p1, p2)
            child = mutate(child, MUTATION_RATE)
            
            new_population.append(child)
            
        # Replace old population with the newly generated one
        population = new_population

    print("Evolution complete!")

    # ==========================================
    # 4. VISUALIZE RESULTS
    # ==========================================
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Target Image")
    plt.imshow(target_image)
    plt.axis("off")
    
    plt.subplot(1, 2, 2)
    plt.title("Reconstructed Image")
    plt.imshow(best_individual)
    plt.axis("off")
    
    plt.show()

if __name__ == "__main__":
    main()