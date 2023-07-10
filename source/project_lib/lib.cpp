#include "lib.h"
#include "internal_subproject/class_x.h"

namespace lib
{

Lib::Lib()
 : x(new internal::X)
{
}

Lib::~Lib()
{
}

void Lib::do_a_thing(int val)
{
   if (x)
   {
      x->set_x(val);
   }
}

void Lib::d_a_const_thing() const
{
}

int Lib::get_x() const
{
   if (x)
   {
      return x->get_x();
   }
   else
   {
      return -1;
   }
}

} // end namepsace lib