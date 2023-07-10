#include <fstream>
#include "messages/example_msg.pb.h"

int main() {
    Sensor sensor;
    sensor.set_name("Laboratory");
    sensor.set_temperature(23.4);
    sensor.set_humidity(68);
    sensor.set_door(Sensor_SwitchLevel_OPEN);
    std::ofstream ofs("sensor.data", std::ios_base::out | std::ios_base::binary);
    sensor.SerializeToOstream(&ofs);
}