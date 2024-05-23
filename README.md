# Ising Model Simulation
## Introduction
The Ising model is a widely used mathematical model in statistical mechanics, particularly in the study of magnetic systems. It describes the behavior of a lattice of spins, which represent magnetic moments in a material. These spins can be in one of two states: "up" or "down". The model considers interactions between neighboring spins, influencing the overall energy of the system.

## Example
_**FIg 1, 50x50 Grid**_

![ising 2 - Made with Clipchamp (2)](https://github.com/thatdavidguy/Ising-Modelling/assets/61171213/655437bb-6a72-4cf3-8e64-eabff6ee4868)

_**Fig 2, 400x400 Grid + Spin Graph + Energy Graph**_

![Untitled video - Made with Clipchamp (3)](https://github.com/thatdavidguy/Ising-Modelling/assets/61171213/b73c4963-0705-4290-8231-03ac4bdf9ca9)

![ising 3](https://github.com/thatdavidguy/Ising-Modelling/assets/61171213/582ce7b2-125e-4cc0-b2bc-d4a292be888b)



## Overview
This Python code simulates the Ising model using the Pygame and NumPy libraries. It provides a visual representation of the lattice and tracks its evolution over time.

## Key Features
Lattice Representation: The lattice is represented as a 2D array, where each cell corresponds to a spin.
Energy Calculation: The energy of the lattice is calculated based on interactions between neighboring spins.
Visualization: The lattice is visualized using Pygame, with each spin represented by a colored square.
## Main Simulation Loop
Initialization: Pygame is initialized, and the initial state of the lattice is displayed.
Main Loop: The simulation runs continuously, updating the lattice based on user input and the rules of the Ising model. Information about the completion percentage, energy, and spin status is displayed on the screen.
## Conclusion
This simulation provides an interactive way to explore the behavior of the Ising model. By visualizing the lattice and tracking its evolution, users can gain insights into the complex dynamics of magnetic systems and emergent phenomena such as phase transitions.
