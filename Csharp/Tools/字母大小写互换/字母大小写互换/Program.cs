using System;

class Program
{
    static void ToggleCase(ref char[] str)
    {
        for (int i = 0; i < str.Length; ++i)
        {
            if (char.IsLower(str[i]))
            {
                str[i] = char.ToUpper(str[i]); // 小写转大写
            }
            else if (char.IsUpper(str[i]))
            {
                str[i] = char.ToLower(str[i]); // 大写转小写
            }
        }
    }

    static void Main()
    {
        Console.Write("请输入需要转换的字符：");
        string input = Console.ReadLine();

        char[] a = input.ToCharArray();

        ToggleCase(ref a); // 调用函数进行大小写转换

        Console.WriteLine("转换结果为：" + new string(a) + Environment.NewLine);

        // 等待用户按下任意键退出程序
        Console.WriteLine("按任意键退出...");
        Console.ReadKey();
    }
}
