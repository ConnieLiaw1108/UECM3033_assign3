import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def system(y, t, a, b):
    y0, y1 = y;
    dydt = [a*(y0-y0*y1), b*(-y1+y0*y1)];
    return dydt;
    
if __name__ == "__main__":
  a = 1.0;
  b = 0.2;
  initial_y = [0.1, 1.0];
  t = np.linspace(0, 5, 101);
  sol = odeint(system, initial_y, t, args=(a,b));
  
  #Plot the graph of y0 and y1 against t
  plt.plot(t, sol[:,0], 'b', label='y0 against t');
  plt.plot(t, sol[:,1], 'r', label='y1 against t');
  plt.title('graph of y0 and y1 against t');
  plt.xlabel('year, t');
  plt.xlabel('y(t)');
  plt.legend(loc='best');
  plt.grid();
  plt.show();
  
  #Plot the graph of y1 against y0
  plt.plot(sol[:,0], sol[:,1], 'g', label='y1 against y0');
  plt.title('graph of y1 against y0');
  plt.xlabel('y0');
  plt.ylabel('y1');
  plt.legend(loc='best');
  plt.grid();
  plt.show();
  
  #Sensitivity part
  a = 1.0;
  b = 0.2;
  initial_y = [0.11, 1.00];
  t = np.linspace(0, 5, 101);
  sol1 = odeint(system, initial_y, t, args=(a,b));
  
  #New graph of y0 and y1 against t
  plt.plot(t, sol1[:,0], 'b', label='y0 against t');
  plt.plot(t, sol1[:,1], 'r', label='y1 against t');
  plt.title('New graph of y0 and y1 against t with initial_y0 = 0.11');
  plt.xlabel('year, t');
  plt.xlabel('y(t)');
  plt.legend(loc='best');
  plt.grid();
  plt.show();
  
  #New graph of y1 against y0
  plt.plot(sol1[:,0], sol1[:,1], 'g', label='y1 against y0');
  plt.title('graph of y1 against y0 with initial_y0 = 0.11');
  plt.xlabel('y0');
  plt.ylabel('y1');
  plt.legend(loc='best');
  plt.grid();
  plt.show();
  
  
  
