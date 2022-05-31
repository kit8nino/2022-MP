import java.util.Scanner;

public class Main
{
    public static void main(String[] args) {

        System.out.println(Method(new Scanner(System.in).nextDouble(), -Math.random() * 1000, Math.random() * 1000));
    }

    public static Double Func(double x, double e) { return (2 - x) * Exp(x, 1, e); }
    public static Double Pow(double x, double save) { return Math.pow(1 + x / save, save); }

    public static Double Exp(double x, double save, double e)
    {

        if((Pow(x, save * 10) - Pow(x,save)) > e)
        {
            return Exp(x, save * 10, e);
        }
        else
        {
            return Pow(x, save);
        }
    }

    public  static Double Method(double e, double a, double b)
    {

       if (Math.abs(Func((a + b) / 2, e) - Func(a, e)) > e || Math.abs(Func((a + b) / 2, e) - Func(b, e)) > e)
       {
             if (Func(a, e) * Func((a + b) / 2, e) < 0)
             {
                 return Method(e, a, (a + b) / 2);
             }
             else
             {
                 return Method(e, (a + b) / 2, b);
             }
       }
       else
       {
           return((a + b) / 2);
       }
    }
}
