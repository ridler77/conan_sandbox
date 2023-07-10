#pragma once

#include <memory>

namespace internal
{
   class X;
}

namespace lib
{

class Lib
{
   public:
      Lib();
      Lib(Lib const &) = delete;
      Lib(Lib &&) = delete;
      Lib & operator=(Lib const &) = delete;
      Lib & operator=(Lib &&) = delete;
      ~Lib();

      void do_a_thing(int val);
      void d_a_const_thing() const;
      int get_x() const;
   
   private:
      std::unique_ptr<internal::X> x;
};

} // end namepsace lib