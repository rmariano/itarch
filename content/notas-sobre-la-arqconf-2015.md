+++
title = "Notas sobre la ArqConf 2015"
slug = "notas-sobre-la-arqconf-2015"
date = 2015-05-01T17:45:37+03:00
[taxonomies]
tags = ['software', 'architecture', 'BigData']
+++

Este es mi resumen sobre la ArqConf 2015, la conferencia sobre
**arquitectura de software** que tuvo lugar en la UCA el 30 de Abril de
2015. La idea es sintetizar las principales ideas que me llevé y
resaltar lo más importante.

Se presentan a continuación un listado de las ideas principales por
charla con un breve listado de lo que más destaco por cada uno. Nótese
que la lista no es de ninguna manera exhaustiva, y cada sección es en
realidad un breve párrafo ilustrativo a modo de resumen muy a alto
nivel.

Cada sección lleva un título alusivo al tema de la presentación, un
breve resumen y una lista con los principales puntos que destaco.

# Orden en una arquitectura y la agilidad como atributo de calidad

Se basó en la experiencia de un arquitecto liderando un equipo de
arquitectura para un desafiante proyecto. El disertante explicó los
problemas a resolver, y el marco tecnológico en el que se desarrolló la
solución, y cómo con una arquitectura elegante y simple con
relativamente pocos componentes se puede llevar a cabo una
implementación de gran porte que de soporte a 150.000 transacciones
concurrentes.

-   El factor clave del éxito de una arquitectura es la comunicación.
-   La agilidad de un equipo como atributo de calidad. Es interesante,
    porque cuando uno piensa en atributos de calidad se le ocurren cosas
    como *seguridad*, *mantenibilidad*, *usabilidad*, *escalabilidad*,
    etc. pero no el hecho de ser ágil. Sin embargo es en general
    deseable que el equipo sea ágil y se pueda adaptar fácilmente a los
    cambios, y en ese caso ¿Por qué no agregarlo como un atributo de
    calidad?
-   La flexibilidad del equipo, también como atributo de calidad.
    Análogo al anterior, pero con un detalle: si es un atributo de
    calidad, tiene que ser *medible*. Lo interesante no es sólo la
    originalidad de este tipo de atributos de calidad \"no
    tradicionales\", sino también en como considerarlos dentro de los
    *escenarios de calidad*.
-   Los requerimientos deben priorizarse en el marco global de la
    organización.

# Arquitectura y Big Data Analytics.

Una presentación excelente, con mucho detalle y riqueza técnica,
nombrando tecnologías, metodologías, técnicas, y estilos de arquitectura
orientados a Big Data.

-   Kafka como herramienta para procesamiento de información en colas de
    mensajes no tradicionales (con estado persistente). Es un ejemplo de
    una tecnología que tuvo un caso de éxito real en proyectos de Big
    Data.
-   Siempre guardar la fuente de datos: llamada *\"la fuente de la
    verdad\"* (*the source of truth*), es una buena práctica, ya que
    tiene varias ventajas, como por ejemplo:
    -   Permite corregir errores en caso de falla (a partir de los
        datos, se puede volver a procesar y no hay una pérdida
        irrecuperable de información).
    -   Preservando los datos originales (*raw data*), es posible en un
        futuro elaborar o calcular nuevas métricas si se requieren, cosa
        que si por el contrario sólo se guardaran los datos procesados,
        sería imposible.
    -   El costo extra por el almacenamiento no debería ser un problema,
        considerando los beneficios.
-   Procesar la información de forma **idempotente**: esta quizá sea la
    idea que mejor refleja una buena práctica general, no solo aplicable
    a Big Data. En lugar de procesar modificando registros (por ejemplo
    ejecutando un SQL que sume uno en alguna columna), simplemente se
    agregue una nueva entrada y luego el resultado se calcule sobre el
    total. De esta manera no se modifican los datos, y de nuevo, un
    potencial error es reparable, no hay pérdida irreversible de
    información, etc. Ésta en realidad es una idea que ya existía en
    sistemas de BI, pero es interesante notar que registrar los *hechos*
    se puede usar para muchos más casos.
-   Simplificar las variables tecnológicas. En lugar de tener un extenso
    repertorio tecnológico con muchas tecnologías de propósito
    específico, es mejor y más fácil de mantener un entorno con menos
    tecnologías, y, aunque estas no se adapten perfectamente a cada
    problema en particular, aún así hay que privilegiar el pragmatismo,
    haciendo los ajustes necesarios.
-   Tener un esquema de datos (*data schema*) para poder integrar la
    información que se procesa desde diferentes fuentes.

# Arquitecturas de Micro servicios.

Es muy interesante escuchar sobre los micro servicios, y cómo este tipo
de arquitecturas permiten una escalabilidad más flexible.

-   Las arquitecturas de micro servicios permiten obtener la misma
    funcionalidad, pero de forma distribuida, en contraposición a lo que
    sería una arquitectura monolítica.
-   Esto permite escalar de forma más flexible, por ejemplo se pueden
    administrar los subsistemas de forma independiente, asignando los
    recursos o manteniendo más componentes pero más simples.
-   Esta separación también puede reflejarse en equipos de trabajo,
    áreas o procesos.

# Arquitectura y métodos ágiles

En esta ocasión, se habló de la arquitectura de software desde el punto
de vista de las metodologías ágiles y los procesos de desarrollo
alineados a los requerimientos funcionales del negocio.

-   El equipo puede conversar la arquitectura en función de los
    requerimientos con el PM, sin necesariamente entrar en muchos
    detalles técnicos, concentrándose en la funcionalidad y
    comportamiento esperado.
-   Ésta conversación sobre la arquitectura debe ser constante a lo
    largo de todo el ciclo de desarrollo.

# Arquitectura aplicada la producción

Excelente cierre de la conferencia. Hizo mucho hincapié en cómo se ve a
la arquitectura y el rol del arquitecto o el equipo de arquitectura
desde el punto de vista del CIO. Ésto dilucidó bastante sobre lo que se
espera del equipo de arquitectura para que la organización funcione.

Lo más destacado fue ver qué es lo que se espera y lo que *NO* se espera
del arquitecto, y cómo lo más importante es poder brindar una solución
como ingenieros, que responda a las necesidades del negocio. La
principal riqueza estuvo en que las ideas fueron ilustradas con
experiencias reales en Data Centers reales.

Algo llamativo es que muchas ideas mencionadas son en realidad
cuestiones que se asumen en un proyecto de software, pero como sabemos
en la práctica no siempre sucede, y esto deriva en malos resultados.

-   La **integridad conceptual** es fundamental: Las soluciones deben
    proporcionarse de forma uniforme, aplicando sendos estilos y
    tecnologías para los mismos tipos de problemas. Análogamente, si
    para diferentes proyectos se usan muchas tecnologías diferentes, el
    resultado es una arquitectura gigante y muy difícil de mantener.
-   Cada componente técnico interno del equipo de ingeniería *no* es el
    principal objetivo de la organización, si no que están para
    responder a éstos.
-   Adoptar nuevas tecnologías solo por que presenta algunas ventajas
    parciales no siempre es una buena idea a largo plazo. Suele suceder
    que a largo plazo termina teniendo consecuencias perjudiciales para
    el proyecto.
-   Los sistemas deben diseñarse y construirse para durar varios años
    (\~10), y esto implica que las tecnologías de construcción tienen
    que tener varios años de existir, de manera que sea razonable
    aseverar que seguirán estando disponibles el tiempo que dure el
    sistema productivo. No sería deseable tener que mantener o hacerse
    cargo de tecnologías (frameworks, toolkits, etc.) obsoletas.
-   Criticar las llamadas *\"buenas prácticas\"* (o *verdades
    reveladas*). Esto significa que cuando algo se denomina como buena
    práctica hay que plantearse si realmente es así, y aunque lo fuera,
    si esas ventajas que trae aplican al proyecto en cuestión. Ésta es
    otra idea más general, se trata en definitiva de tener *pensamiento
    crítico*, pero es algo que en muchos casos no sucede, y vemos en
    general varios proyectos aplicando \"patrones de diseño\" (o de
    arquitectura) o \"buenas prácticas ágiles\", etc. sin pensar
    realmente cómo aplican al proyecto (algo puede haber dado resultados
    excelentes en otro proyecto, en otra empresa, en otro país, pero el
    arquitecto debe considerar si esas variables realmente coinciden o
    son relevantes al contexto).

# \>\>\> Conclusiones

Considero que la conferencia fue muy buena, teniendo en cuenta la
calidad de las presentaciones, la experiencia de los disertantes y que
todo estaba alienado conceptualmente, lo cual hizo que la transición
entre temas tuviera una continuidad notable.

Es además importante destacar que este tipo de conferencias, además de
ser enriquecer la experiencia profesional de todos (disertantes,
organizadores y concurrentes), benefician a la comunidad de arquitectos.
