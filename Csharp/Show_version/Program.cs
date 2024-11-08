using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

partial class Program
{
    static void Main()
    {
        // 获取当前程序的目录
        string scriptDir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
        string configFile = Path.Combine(scriptDir, "config.ini");

        // 读取配置文件
        string majorVersion = "";
        string statusOrRevision = "";
        try
        {
            using StreamReader sr = new(configFile, Encoding.UTF8);
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                // 使用正则表达式来匹配配置项信息，并且传递 RegexOptions.Compiled 选项
                Match match = MyRegex().Match(line);
                if (match.Success)
                {
                    string key = match.Groups["key"].Value.Trim().ToLower();
                    string value = match.Groups["value"].Value.Trim();

                    if (key == "major_version_number")
                    {
                        majorVersion = value;
                    }
                    else if (key == "status_or_revision_number")
                    {
                        statusOrRevision = value;
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine($"无法读取配置文件：{ex.Message}");
            Console.ResetColor();
            Environment.ExitCode = 1;
            return;
        }

        // 输出
        Console.WriteLine("--------------芙芙工具箱-------------");
        Console.WriteLine("-> Code by 鸭鸭「カモ」/ DuckStudio");
        Console.WriteLine($"Version: v{majorVersion}-{statusOrRevision}");
        Console.WriteLine("-------------------------------------");

        Console.WriteLine("按任意键继续...");
        Console.ReadKey();
    }

    [GeneratedRegex(@"^\s*(?<key>\w+)\s*=\s*(?<value>.*)$", RegexOptions.Compiled)]
    private static partial Regex MyRegex();
}
