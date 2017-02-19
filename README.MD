# Hashcode

## Practice session: Specification

1. Find number of M's and T's
    ```java
       int countMT(String filename); 
    ```
2. Given mushroom coordinate, find all possible groupings around the mushroom
    ```java
       List<Mushroom> groupMushrooms(L, H, mushroom);
    ```
3. Given matrix and mushroom grouping, find corresponding maximising matrices
     ```java
       int[][] newMatrices(matrix, List<mushroom>);
    ```
4. Find edges of given matrix
    ```java
        List<Edge> findEdges(matrix);
    ```
5. Given edge, find nearest mushroom coordinate
    ```java
        Mushroom findNearestMushroom(matrix, edge);
    ```

## Code Paste Bin

File: small.in
```
6 7 1 5
TMMMTTT
MMMMTMM
TTMTTMT
TMMTMMM
TTTTTTM
TTTTTTM
```

Python Greedy Rand implementation

**NOTE:** `check_slice_condition` is incomplete for now

```python

'''
    Greedy implementation 1
    Global data structure:
        slice: tuple ( (row1, column1), (row2, column2) )
        config: {
                row: pizza_row,
                column: pizza_column,
                L: minimum element on each slice,
                H: maximum cells
        }
        pizza[][]: 1== M, 2==T
'''

from random import randint

def load_in_data(filename):
    '''
        Load input data
        Data structure: array of columns of T's and M's
         T==>2 ; M==> 1
    '''
    # Array of input data
    input_data = open(filename).readlines();
    pizza_config = input_data[0].split();
    config = dict(row=pizza_config[0],column=pizza_config[1],L=pizza_config[2],H=pizza_config[3]);
    del input_data[0];
    for i in range(len(input_data)):
        # remove line breaks
        input_data[i] = input_data[i].replace("\n","");
        input_data[i] = input_data[i].replace("T","2"); #Tomato==2
        input_data[i] = input_data[i].replace("M","1");
        input_data[i] = [int(ch) for ch in input_data[i]];
    return config, input_data;

def check_overlap(slices, new_slice):
    '''
        check for overlaps returning true if overlap exists
        takes arguments pizza, current slices and the new slice
        slice: tuple ( (row1, column1), (row2, column2) )
    '''

    if slices[0] == None:
        return False;
    for s in slices:
        # condition for overlap: any corner falls in the area of an existing slice
        # check every corner
        for corner in new_slice:
            if corner[0] > s[0][0] and corner[0] < s[1][0] and corner[1] > s[0][1] and corner[1] < s[1][1]:
                return True;
    return False;

def check_slice_condition(pizza, config, new_slice):
    '''
        check that the slice meets the minimum TM condition and the maximum size condition
    '''
    row1 = new_slice[0][0];
    row2 = new_slice[1][0];
    column1 = new_slice[0][1];
    column2 = new_slice[1][1];
    if (row2 - row1 + 1) * (column2 - column1 + 1) > config.H :
        return False;
    MCount = 0;
    TCount = 0;
    for pizzaRow in pizza:
        


if __name__ == "__main__":
    print(load_in_data("small.in"));

```



Initialisation code
```java=
package hashcode_practice;
import java.util.*;
import java.io.*;

/**
 *
 * @author einsteinly
 */
public class Hashcode_practice {
    public static boolean[][] pizza;
    public static int pizza_row;
    public static int pizza_column;
    public static int L;
    public static int H;
    public static int MCount;
    public static int TCount;
    
    public static void initialisePizza(String filename) throws FileNotFoundException{
        String raw_data = new Scanner(new File(filename)).useDelimiter("\\Z").next();
        String[] file_lines = raw_data.split("\n");
        //get data from first line
        String[] pizza_config = file_lines[0].split("\\s+");
        
        pizza_row = Integer.parseInt(pizza_config[0]);
        pizza_column = Integer.parseInt(pizza_config[1]);
        L = Integer.parseInt(pizza_config[2]);
        H = Integer.parseInt(pizza_config[3]);
        
        String[][] pizza_data = new String[pizza_row][pizza_column];
        for(int i=1;i< file_lines.length;i++){
            pizza_data[i-1] = file_lines[i].split("");
        }
        pizza = new boolean[pizza_row][pizza_column];
        for(int row=0;row<pizza_row;row++){
            for(int column=0;column<pizza_column;column++){
                if(pizza_data[row][column].compareTo("T") == 0) pizza[row][column]=false;
                else pizza[row][column]=true;
            }
        }
    }
    
    public static boolean countMT() throws FileNotFoundException{
                
        MCount = 0;
        TCount = 0;
        for(boolean[] row:pizza){
            for(boolean element:row){
                if(element) MCount++;
                else TCount++;
            }
        }
        // return the smaller element T==> false, M==>true
        if(TCount >= MCount) return true;
        else return false;
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException {
        // TODO code application logic here
        initialisePizza("small.in");
        System.out.print(countMT());
    }
    
}



```



## Practice session: Notes
- mushroom ==> true
- tomatoes ==> false










## Languages of choice

| Language | Level of Preference | Level of proficiency | Your name |
| --- | --- | --- | --- |
| Python3 | Highly preferable | most proficient | einsteinly |
| C / C++ | Okay with it | know a bit | einsteinly |
| --- | --- | --- | --- |
|Python2.7|用了几年|     | Sifang|
|Java | | | Sifang|
| --- | --- | --- | --- |
|C| Preferred|Proficient for algorithmic purpose|Penguin|
|Java|Preferred|Proficient for OOP purpose|Penguin|
|C++|Not preferred|basic knowledge|Penguin|
## Deadlines and time

==***Note: CET === GMT + 1***==

 - Registration: 20th February 2017 18:00 CET (17:00 GMT)


 - Online Qualification Round:
    Thursday,
    23rd February 2017
    18:30 to 22:30 CET
    (17:30 to 21:30 GMT)
    
    
- Final Round:
    Saturday,
    1st April 2017
    9:30 to 21:30 CET

## Notes

https://hashcode.withgoogle.com/past_editions.html

