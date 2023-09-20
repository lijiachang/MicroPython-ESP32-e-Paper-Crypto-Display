# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import sleepscheduler as sl
import get_symbol_price_to_display

sl.schedule_on_cold_boot(get_symbol_price_to_display.init_on_cold_boot)
sl.run_forever()