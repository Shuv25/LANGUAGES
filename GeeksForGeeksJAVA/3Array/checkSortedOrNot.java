import java.util.*;
public class checkSortedOrNot {

  public static boolean isSorted(int size,int arr[])
  {
    for(int i=0;i<size;i++)
    {
        for(int j=i+1;j<size;j++)
        {
            if(arr[i]>arr[j])
            {
                return false; 
            }
        }
    }
    return true;
  }
  public static int SumOfArray(int size,int arr[]) 
  {
        int ans=0;
        for(int i=0;i<size;i++)
        {
            ans+=arr[i];
        }
        return ans;
  }
  public static int avgOfArray(int size,int arr[]) 
  {
        int ans=0;
        for(int i=0;i<size;i++)
        {
            ans+=arr[i];
        }
        return ans/arr.length;
  }
  public static void main(String[] args) 
  {
    Scanner sc=new Scanner(System.in);
    System.err.print("Size:");
    int size=sc.nextInt();
    int arr[]=new int[size];
    System.out.print("elements of the array:");
    for(int i=0;i<size;i++)
    {
        arr[i]=sc.nextInt();
    }
    if(isSorted(size,arr))
    {
        System.err.println("Array is sorted");
    }
    else
    {
        System.err.println("Array is not sorted");
    }

    System.out.println("Sum of the array is :"+SumOfArray(size,arr));
    System.out.println("Average of the array is :"+avgOfArray(size,arr));
  }  
}
