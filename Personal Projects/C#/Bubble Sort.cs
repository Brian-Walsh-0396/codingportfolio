using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        // Generate 100 random numbers between 1 and 100
        int[] numbers = Enumerable.Range(1, 100).OrderBy(x => Guid.NewGuid()).ToArray();

        // Print the unsorted numbers
        Console.WriteLine("Unsorted numbers:");
        Console.WriteLine(string.Join(", ", numbers));

        // Bubble sort the numbers in ascending order
        for (int i = 0; i < numbers.Length - 1; i++)
        {
            for (int j = 0; j < numbers.Length - i - 1; j++)
            {
                if (numbers[j] > numbers[j + 1])
                {
                    int temp = numbers[j];
                    numbers[j] = numbers[j + 1];
                    numbers[j + 1] = temp;
                }
            }
        }

        // Print the sorted numbers
        Console.WriteLine("Sorted numbers:");
        Console.WriteLine(string.Join(", ", numbers));

        // Wait for user input
        Console.ReadLine();
    }
}
