#pragma once

template<typename T>
class A
{
public:
   
   A(std::string const & s) : s(s) {};

   std::string get_string() const
   {
      return s;
   }

   T square(T x)
   {
      val = x;
      return x * x;
   }

private:
   std::string s = "";
   T val;
   
};