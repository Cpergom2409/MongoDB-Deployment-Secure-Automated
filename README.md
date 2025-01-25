# MongoDB-Deployment-Secure-Automated

Este proyecto tiene como objetivo proporcionar una solución automatizada y segura para desplegar y gestionar una infraestructura MongoDB basada en contenedores Docker. Combina herramientas de monitorización, backup y gestión para garantizar la disponibilidad, la integridad y la eficiencia en el manejo de bases de datos.

🚀 Funcionalidades Principales

Replicaset MongoDB:

Implementación de un replicaset compuesto por 4 nodos para alta disponibilidad y tolerancia a fallos.
Sincronización en tiempo real y distribución de lecturas en nodos secundarios.
Flask y PyMongo:

Panel de administración para gestión de usuarios y contraseñas con autenticación segura.
Panel de clientes para consulta de datos con interfaces HTML/CSS y scripts backend en PyMongo.
Mongo Express:

Interfaz gráfica para operaciones CRUD, gestión de índices y monitoreo básico de bases de datos.
Monitorización:

Prometheus y Grafana: Recolección y visualización de métricas.
AlertManager y Discord: Sistema de alertas en tiempo real.
Loki y Promtail: Gestión y visualización de logs.
Backup y Seguridad:

Copias de seguridad automáticas con Duplicati y almacenamiento en Google Drive.
Proxy inverso y certificados SSL mediante Nginx Proxy Manager.

📂 Estructura del Proyecto

El proyecto está completamente automatizado y se gestiona mediante archivos YAML. Se incluye un manual detallado con los pasos para desplegar y configurar la infraestructura, disponible en el archivo PDF adjunto al repositorio.

Servicios Incluidos
MongoDB Replicaset
Flask con PyMongo
Mongo Express
Prometheus, Grafana, Loki y AlertManager
Duplicati para copias de seguridad
Nginx Proxy Manager para securizar el acceso

📜 Manual de Uso

Para más detalles, consulta el manual adjunto en este repositorio: [Nombre_del_archivo].pdf. Incluye:

Configuración inicial
Ejemplos de código
Pruebas funcionales
Guía paso a paso para desplegar la infraestructura.

👤 Contacto

Si tienes dudas, sugerencias o deseas contribuir al proyecto, no dudes en contactarme:

Creador: Cristian Pérez Gómez
Email: cpergom2409@gmail.com
Linkedin: www.linkedin.com/in/cristian-pérez-356961262

¡Agradezco cualquier aportación de la comunidad!
