import pygame
import numpy as np
import time
import numpy as np
from scipy.ndimage import convolve, generate_binary_structure
import matplotlib.pyplot as plt

color_bg = (10,10,10)
color_grid = (40,40,40)
color_die_next = (170,170,170)
color_alive_next = (255,255,255)



def get_energy_arr(lattice):
    # applies the nearest neighbours summation
    kern = generate_binary_structure(2, 1) 
    kern[1][1] = False
    arr = -lattice * convolve(lattice, kern, mode='constant', cval=0)
    return arr

def get_energy(lattice):
    return get_energy_arr(lattice).sum()

def get_dE_arr(lattices):
    return -2*get_energy_arr(lattices)


def draw(screen, cells, size):
    for row, col in np.ndindex(cells.shape):
        if cells[row, col] == 1:
            pygame.draw.rect(screen, color_alive_next, (col * size, row * size, size - 1, size - 1))
        #else:
         #   pygame.draw.rect(screen, color_bg, (col * size, row * size, size - 1, size - 1))


def main(N,times,BJ):

    start_timer = time.time()
    
    pygame.init()
    size = 2
    screen = pygame.display.set_mode((N*size,N*size))    

    screen.fill(color_grid)

    spin_arr = np.zeros((N, N))
    init_random = np.random.random((N,N))
    spin_arr[init_random>=0.5] = 1
    spin_arr[init_random<0.5] = -1
    draw(screen,spin_arr,size)

    pygame.display.flip()
    pygame.display.update()


    net_spins = []
    net_energy = []

    energy = get_energy(spin_arr)
    print("Initial Energy:",energy)

    running = False
    iterations = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    end_timer = time.time()
                    total_time = end_timer - start_timer
                    return(net_spins,net_energy)
                except:
                    return(net_spins,net_energy)
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    draw(screen,spin_arr,size)
                    pygame.display.update()

        screen.fill(color_grid)
        draw(screen,spin_arr,size)
        if running:
            iterations += 1
            if iterations>times:
                return(net_spins,net_energy)
            completion_percentage = (iterations / times) * 100
            if completion_percentage % 1 == 0: 
                spin_total = spin_arr.sum()
                if spin_total>0:
                    spin_total_precent = (spin_total*100)/(N*N)
                    print(f"Completion: {completion_percentage:.0f}%\t\tEnergy: {get_energy(spin_arr)}\t\t {spin_total_precent}% Up Spin")
                elif spin_total==0:
                    print(f"Completion: {completion_percentage:.0f}%\t\tEnergy: {get_energy(spin_arr)}\t\t Equal Spin")
                else:
                    spin_total_precent = (spin_total*-100)/(N*N)
                    print(f"Completion: {completion_percentage:.0f}%\t\tEnergy: {get_energy(spin_arr)}\t\t {spin_total_precent}% Down Spin")

            i = np.random.randint(0,2)
            j = np.random.randint(0,2)
            dE = get_dE_arr(spin_arr)[i::2,j::2]
            change = (dE>=0)*(np.random.random(dE.shape) < np.exp(-BJ*dE)) + (dE<0)
            spin_arr[i::2,j::2][change] *=-1


            net_energy.append(get_energy(spin_arr))
            net_spins.append(spin_arr.sum()/N**2)
            pygame.display.update()

        #time.sleep(0.001)

def plot_simulation(net_spins, net_energy, beta_J):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    ax = axes[0]
    ax.plot(net_spins)
    ax.set_xlabel('Algorithm Time Steps')
    ax.set_ylabel(r'Average Spin $\bar{m}$')
    ax.grid()
    
    ax = axes[1]
    ax.plot(net_energy)
    ax.set_xlabel('Algorithm Time Steps')
    ax.set_ylabel(r'Energy $E/J$')
    ax.grid()
    
    fig.tight_layout()
    fig.suptitle(fr'Evolution of Average Spin and Energy for $\beta J = ${beta_J}', y=1.07, size=18)
    plt.show()
 
if __name__ == '__main__':
    net_spins,net_energy = main(400,10000,0.7)
    plot_simulation(net_spins, net_energy, 0.7)