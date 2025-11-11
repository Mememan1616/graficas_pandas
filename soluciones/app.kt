package com.example.aquasecurev3

import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.drawerlayout.widget.DrawerLayout
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.navigation.NavigationView
import org.eclipse.paho.android.service.MqttAndroidClient
import org.eclipse.paho.client.mqttv3.IMqttActionListener
import org.eclipse.paho.client.mqttv3.IMqttToken
import org.eclipse.paho.client.mqttv3.MqttMessage
import org.eclipse.paho.client.mqttv3.MqttConnectOptions




class MainActivity : AppCompatActivity() {

    private lateinit var drawerLayout: DrawerLayout
    private lateinit var navView: NavigationView
    private lateinit var client: MqttAndroidClient
    private val brokerUri = "ssl://a694301d890f4537964540f7d9977b9d.s1.eu.hivemq.cloud:8883"
    private val userName = "Mememan1616"
    private val password = "Sans#150"
    private val topic = "control-led"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Inicializar cliente MQTT
        val clientId = "androidClient_" + System.currentTimeMillis()
        client = MqttAndroidClient(this, brokerUri, clientId)
        
        drawerLayout = findViewById(R.id.drawer_layout)
        navView = findViewById(R.id.nav_view)
        val btnMenu = findViewById<FloatingActionButton>(R.id.btnMenu)
        val btn1= findViewById<Button>(R.id.btn_on)
        val btn2 = findViewById<Button>(R.id.btn_off)

        // Opciones de conexión
        val options = MqttConnectOptions()
        options.userName = userName
        options.password = password.toCharArray()
        options.isAutomaticReconnect = true
        options.isCleanSession = true

        // Conectar al broker
        client.connect(options, null, object : IMqttActionListener {
            override fun onSuccess(asyncActionToken: IMqttToken?) {
                // Conectado exitosamente
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                exception?.printStackTrace()
            }
        })
        enableEdgeToEdge()

        // Ajuste de insets para Edge-to-Edge
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main_content)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // Abrir Drawer al presionar botón flotante
        btnMenu.setOnClickListener {
            drawerLayout.openDrawer(navView)
        }
        // Manejar clicks del Drawer
        navView.setNavigationItemSelectedListener { menuItem ->
            when(menuItem.itemId){
                R.id.nav_home -> { /* Acción Home */ }
                R.id.nav_settings -> { /* Acción Settings */ }
                R.id.nav_about -> { /* Acción About */ }
            }
            drawerLayout.closeDrawers()
            true
        }

        btn1.setOnClickListener {
           // enviarMensaje("1")
            print("1")
        }
        btn2.setOnClickListener {
           // enviarMensaje("0")
            print("0")
        }
    }

   /* private fun enviarMensaje(mensaje: String) {
        try {
            val mqttMessage = MqttMessage()
            mqttMessage.payload = mensaje.toByteArray()
            client.publish(topic, mqttMessage)
        } catch (e: Exception) {
            e.printStackTrace()
        }*/
}
}


