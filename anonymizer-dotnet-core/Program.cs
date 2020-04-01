using System;

namespace anonymizer_dotnet_core
{
    class Program
    {
        static void Main(string[] args)
        {
            if(args.Length() == 2)
            {

            }
            else
            {
                Console.WriteLine("Expected 2 arguments: folder path header JSON array");
            }
            Console.WriteLine(args[0]);
            Console.WriteLine(args[1]);
            
            Console.WriteLine("Hello World!");
            
        }
    }
}
