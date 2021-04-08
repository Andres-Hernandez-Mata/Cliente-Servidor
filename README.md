# Cliente-Servidor
Conexiones remotas cliente-servidor

# Cliente UDP
Toda comunicación requiere que se establezca de antemano un protocolo. El protocolo que implementaremos en este chat es sencillo: una sesión de preguntas y respuestas. El cliente solicitará conectarse con el servidor y, una vez conectados, se enviarán mensajes alternando uno a la vez (es decir, uno no puede responder sino hasta que el otro haya respondido) comenzando con el cliente haciendo una pregunta. Para finalizar la comunicación, el cliente simplemente escribirá “bye” y la conexión terminará.

