import java.util.ArrayList;
import java.util.Random;

public class Main {

    static  int N;
    static int n=20 ;
    static int count_sample=5;
    static ArrayList<Integer> sample = new ArrayList<Integer>();
    static int[] count = new int[n];

    public static ArrayList<Integer>  getNextStream(int n)
    {
        ArrayList<Integer> stream = new ArrayList<Integer>();
        Random rn = new Random();

        int i=0;
        while(i<n)
        {
            int random_value = rn.nextInt(N);
            if (stream.indexOf(random_value)==-1)
            {
                stream.add(random_value);
                i++;
            }
        }
        return stream;

    }

    public static void updateSample(int streamItem ,int itemNumber)
    {
        if (itemNumber<=count_sample)
        {
            if (sample.size()==count_sample)
            {
                Random rn = new Random();
                int valtoremove = rn.nextInt(5);
                sample.remove(valtoremove);
            }
            sample.add(streamItem);
            count[itemNumber]++;
        }
        else
        {
            Random rn = new Random();
            double probability = rn.nextDouble();

            if (probability<=((double)count_sample/itemNumber))
            {
                if (sample.size() == count_sample) {
                    int valtoremove = rn.nextInt(5);
                    sample.remove(valtoremove);
                }
                sample.add(streamItem);
                count[itemNumber]++;
            }
        }
    }


    public static void main(String[] args)
    {
        int[] num_tweets = {100, 500, 1000, 10000};

        for (int i=0; i<4; i++)
        {
            N=num_tweets[i];
            ArrayList<Integer> stream = new ArrayList<Integer>();
            stream = getNextStream(n);

            for (int j=0; j<100;j++)
            {
                Random rn = new Random();
                int random_index = rn.nextInt(n);
                updateSample(stream.get(random_index), random_index);
            }
            System.out.println("N = "+N);
            for (int j=0; j<n;j++){
                System.out.print("A"+(j+1)+" = "+count[j]+" ");
            }
            System.out.println();
        }


    }
}
