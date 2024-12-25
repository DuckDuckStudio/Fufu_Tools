using System.Diagnostics;

namespace FufuTools
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 打开 "D:\Duckhome\apps\osukps\osukps.exe"
            Process.Start(@"D:\Duckhome\apps\osukps\osukps.exe");
        }
    }
}
