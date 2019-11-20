import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class End_of_file {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int j = 1;
        Vector<String> str = new Vector<String>();
        Scanner scanner = new Scanner(System.in);

            String y = scanner.nextLine();
            str.add(y);
        while(scanner.hasNext()){
            String n = scanner.nextLine();
            str.add(n);
           
            
        
    }
      
      
        for(int i = 0; i<str.size();i++){
            System.out.println(j+" "+str.get(i));
            j++;
        }
        scanner.close();
}

}
