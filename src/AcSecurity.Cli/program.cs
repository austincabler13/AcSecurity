using AcSecurity.Core;

Console.WriteLine("AcSecurity 2.0");
Console.WriteLine("Application Security Scanner");

FileScanner fileScanner = new FileScanner();

bool exists = fileScanner.FileExists("path/to/file");
Console.WriteLine("File exists: " + exists);