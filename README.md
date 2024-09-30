# python
daily python 
#purpose of this project is adding daily works to the github and in time making improvments to them



void sort(int a[],int b,int c){
    if (b==c)
    {
        return ;
    }
    else{
        int temp1 =b;
        if (b<=c)
        {
            if (a[b]>a[b+1])
            {
                int temp = a[b];
                a[b] = a[b+1];
                a[b+1] =temp;
            }
            b++;   
        }
        b =temp1;
        return sort(a,b+1,c);
    }  
}
