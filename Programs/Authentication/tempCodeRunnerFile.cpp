#include<iostream>
#include<unordered_map>
using namespace std;
bool is_present(char k)
{
   char vowels[]={'a','e','i','o','u'};
    for(int i=0;i<5;i++)
    {
        if(k==vowels[i])
        {
            return true;
        }
    }
    return false;
}
char vowel(string l)
{
   char ans='z';
   for(int i=0;i<l.size();i++)
   {
       if(l[i]<ans and is_present(l[i]))
       {
           ans=l[i];
       }
   }
   return ans;

}
int main()
{
unordered_map<string,char>hm;
int n;
cin>>n;
string list1[n];
for(int i=0;i<n;i++)
{
    cin>>list1[i];
    hm.insert({list1[i],vowel(list1[i])});
}
for(int i=0;i<n-1;i++)
{
    int k=i;
    if(hm[list1[i]]=='z')
        {
            while(k>0 and hm[list1[k-1]]!='z')
            {
                swap(list1[k],list1[k-1]);
                k--;
            }
            continue;
        }
    for(int j=i;j>=0;j--)
    {
        
        if(hm[list1[j]]>hm[list1[j+1]])
        {
            swap(list1[j],list1[j+1]);
        }
        else
        break;
    }
}
for(int i=0;i<n;i++)
{
    cout<<list1[i]<<endl;
}
}