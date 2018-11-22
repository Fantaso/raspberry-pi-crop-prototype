import smbus, time, sys

class Chirp:
        def __init__(self, bus=1, address=0x20):
                self.bus_num = bus
                self.bus = smbus.SMBus(bus)
                self.address = address

        def get_reg(self, reg):
                # read 2 bytes from register
                val = self.bus.read_word_data(self.address, reg)
                # return swapped bytes (they come in wrong order)
                return (val >> 8) + ((val & 0xFF) << 8)

        def reset(self):
                # To reset the sensor, write 6 to the device I2C address
                self.bus.write_byte(self.address, 6)

        def set_addr(self, new_addr):
                # To change the I2C address of the sensor, write a new address
                # (one byte [1..127]) to register 1; the new address will take effect after reset
                self.bus.write_byte_data(self.address, 1, new_addr)
                self.reset()
                self.address = new_addr

        def moist(self):
		# To read soil moisture, read 2 bytes from register 0
                moist_not_calibrated = self.get_reg(0) # get moist not calibrated
                if moist_not_calibrated < 355:
                        moist_calibrated = 0
                        return moist_calibrated
                elif moist_not_calibrated > 790:
                        moist_calibrated = 100
                        return moist_calibrated
                else:
                        moist_calibrated = ( moist_not_calibrated - 355 ) / 4.35 # calibrate moist sensor
                        return moist_calibrated # return moist calibrated
		#return self.get_reg(0) # return moist not calibrated

                #def moist_conditioning(self):
                #moist_conditioning = ( self - 355 ) / 4.35
                #print str(moist_conditioning) 
                
        def temp(self):
                # To read temperature, read 2 bytes from register 5
                temp_not_cal = self.get_reg(5) # not calibrated
                temp_cal = temp_not_cal / 10 # calibrated
                return temp_cal         #return calibrate temperature
                #return self.get_reg(5) # return temperature not calibrated

        def light(self):
                # To read light level, start measurement by writing 3 to the
                # device I2C address, wait for 3 seconds, read 2 bytes from register 4
                self.bus.write_byte(self.address, 3)
                time.sleep(1.5)
                return self.get_reg(4)

        def __repr__(self):
                return "<Chirp sensor on bus %d, addr %d>" % (self.bus_num, self.address)

#moist= Chirp()
#print (moist.moist())

'''
if __name__ == "__main__":
	addr = 0x20
	if len(sys.argv) == 2:
		if sys.argv[1].startswith("0x"):
			addr = int(sys.argv[1], 16)
		else:
			addr = int(sys.argv[1])
	chirp = Chirp(1, addr)

	#print chirp
	#print "Moisture\tTemperature\tBrightness"
	#while True:
        Moist = (chirp.moist())
        moist_conditioning = str(( Moist - 355 ) / 4.35)
        Temp = str(chirp.temp())        
        Light = (chirp.light())

        print "  Moist = " + str(Moist) + "   %"
        print "  Moist = " + moist_conditioning[:5] + " %"
        print "  Temp  = " + Temp[0:2] + "." + Temp[2] + "  C"
        #print "  Light = " + str(chirp.light()) + " lx"
		#print "%d\t%d\t%d" % (chirp.moist(), chirp.temp(), chirp.light())
	#	time.sleep(1)
'''
