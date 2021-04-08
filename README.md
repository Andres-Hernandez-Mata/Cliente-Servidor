# Cliente-Servidor
Conexiones remotas cliente-servidor

## Cliente UDP
Toda comunicación requiere que se establezca de antemano un protocolo. El protocolo que se implementa en este chat es sencillo: una sesión de preguntas y respuestas. El cliente solicitará conectarse con el servidor y, una vez conectados, se enviarán mensajes alternando uno a la vez (es decir, uno no puede responder sino hasta que el otro haya respondido) comenzando con el cliente haciendo una pregunta. Para finalizar la comunicación, el cliente simplemente escribirá “bye” y la conexión terminará.

## Servidor UDP
Siguiendo con el protocolo de preguntas y respuestas, el servidor UDP recibe las preguntas del cliente y se envian las respuestas.