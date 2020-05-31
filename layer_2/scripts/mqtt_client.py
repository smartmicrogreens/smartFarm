import constants as ct
# We import the module to publish messages via MQTT
import paho.mqtt.publish as publish
# We import the module to subscribe to MQTT topics
import paho.mqtt.subscribe as subscribe

# We initialize the MQTT client
publish.single("casa/comedor/temperatura", payload="Este es otro mensaje de prueba", hostname=ct.MQTT_BROKER)

# We define a function to receive the messages
def on_msg_print(client, userdata, message):
    if(message.topic == "paho/test/callback"):
        print("%s %s" % (message.topic, message.payload))
    else:
        print("Unrecognized topic bb")

# We subscribe to a topic and process its replies with "on_msg_print"
subscribe.callback(on_msg_print, "paho/test/#", hostname=ct.MQTT_BROKER)