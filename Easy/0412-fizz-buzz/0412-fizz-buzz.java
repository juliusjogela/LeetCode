class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> answer = new ArrayList<>();
        for(int i = 1; i <= n; i++)
        {
            if( (i % 3 == 0) && !(i % 5 == 0))   //If divisible by 3 and not 5: Fizz
            {
            answer.add("Fizz");
            }
            if( (i % 5 == 0) && !(i % 3 == 0))  //If divisible by 5 and not 3: Buzz
            {
            answer.add("Buzz");
            }
            if( (i % 5 == 0) && (i % 3 == 0))//If divisible by 5 and 3: FizzBuzz
            {
            answer.add("FizzBuzz");
            }
            if( !(i % 5 == 0) && !(i % 3 == 0))//If divisible by not 3 and not 5 Int as String
            {
            answer.add(String.valueOf(i));
            }
        }
        System.out.println("Answer is: " + answer);
        return answer;
    }
}