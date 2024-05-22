import pygame
import numpy as np
import time
import numpy as np
from scipy.ndimage import convolve, generate_binary_structure

color_bg = (10,10,10)
color_grid = (40,40,40)
color_die_next = (170,170,170)
color_alive_next = (255,255,255)



def get_energy(lattice):
    # applies the nearest neighbours summation
    kern = generate_binary_structure(2, 1) 
    kern[1][1] = False
    arr = -lattice * convolve(lattice, kern, mode='constant', cval=0)
    return arr.sum()

def draw(screen, cells, size):
    for row, col in np.ndindex(cells.shape):
        if cells[row, col] == 1:
            pygame.draw.rect(screen, color_alive_next, (col * size, row * size, size - 1, size - 1))
        #else:
         #   pygame.draw.rect(screen, color_bg, (col * size, row * size, size - 1, size - 1))

def draw_single_cell(screen, x, y, new_spin, size):
    if new_spin == -1:
        color = color_die_next
        pygame.draw.rect(screen, color, (x * size, y * size, size - 1, size - 1))
    else:
        color = color_grid
        pygame.draw.rect(screen, color, (x * size, y * size, size - 1, size - 1))

def main(N,times,BJ):

    start_timer = time.time()
    
    pygame.init()
    screen = pygame.display.set_mode((N*10,N*10))    
    screen.fill(color_grid)

    spin_arr = np.zeros((N, N))
    init_random = np.random.random((N,N))
    spin_arr[init_random>=0.5] = 1
    spin_arr[init_random<0.5] = -1
    draw(screen,spin_arr,10)

    pygame.display.flip()
    pygame.display.update()


    net_spins = np.zeros(times)
    net_energy = np.zeros(times)

    energy = get_energy(spin_arr)
    print("Initial Energy:",energy)

    running = False
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    end_timer = time.time()
                    total_time = end_timer - start_timer
                    return(0)
                except:
                    return(0)
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    draw(screen,spin_arr,10)
                    pygame.display.update()

        screen.fill(color_grid)
        draw(screen,spin_arr,10)
        if running:
            i += 1
            if i>times:
                return(0)
            completion_percentage = (i / times) * 100
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

            x = np.random.randint(0,N)
            y = np.random.randint(0,N)
            spin_i = spin_arr[x,y] #initial spin
            spin_f = spin_i*-1 #proposed spin flip

            E_i = 0
            E_f = 0
            if x>0:
                E_i += -spin_i*spin_arr[x-1,y]
                E_f += -spin_f*spin_arr[x-1,y]
            if x<N-1:
                E_i += -spin_i*spin_arr[x+1,y]
                E_f += -spin_f*spin_arr[x+1,y]
            if y>0:
                E_i += -spin_i*spin_arr[x,y-1]
                E_f += -spin_f*spin_arr[x,y-1]
            if y<N-1:
                E_i += -spin_i*spin_arr[x,y+1]
                E_f += -spin_f*spin_arr[x,y+1]

            # 3 / 4. change state with designated probabilities
            dE = E_f-E_i
            if (dE>0)*(np.random.random() < np.exp(-BJ*dE)):
                draw_single_cell(screen, x, y, spin_f, 10)
                spin_arr[x,y]=spin_f
                energy += dE
            elif dE<=0:
                spin_arr[x,y]=spin_f
                energy += dE

            net_spins[i-1] = spin_arr.sum()
            net_energy[i-1] = energy
            pygame.display.update()

        #time.sleep(0.001)

 
if __name__ == '__main__':
    main(50,1000000,0.7)
    pass