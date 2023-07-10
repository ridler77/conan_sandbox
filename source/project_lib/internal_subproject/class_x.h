#pragma once 

namespace internal
{
   class X
   {
   public:
      void set_x(int x);
      int get_x() const;

   private:
      int x = 0;
   };
}