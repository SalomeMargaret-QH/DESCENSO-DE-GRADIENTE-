
library(shiny)
library(rsconnect)


# Función objetivo (parábola)
objetivo <- function(x) {
  return((x - 3)^2 + 4)
}

# Derivada de la función objetivo
objetivo_derivada <- function(x) {
  return(2 * (x - 3))
}

# Implementación del descenso de gradiente
descenso_gradiente <- function(punto_inicial, tasa_aprendizaje, iteraciones) {
  historial <- numeric(iteraciones + 1)
  historial[1] <- punto_inicial
  
  for (i in 1:iteraciones) {
    gradiente <- objetivo_derivada(historial[i])
    nuevo_punto <- historial[i] - tasa_aprendizaje * gradiente
    historial[i + 1] <- nuevo_punto
  }
  return(historial)
}

# Interfaz de usuario
ui <- fluidPage(
  titlePanel("Descenso de Gradiente"),
  
  sidebarLayout(
    sidebarPanel(
      h3("Concepto:"),
      p("El algoritmo de descenso de gradiente es una técnica iterativa que permite encontrar el mínimo de una función. Cada paso mueve el valor actual en la dirección opuesta a la pendiente o gradiente de la función."),
      p("En este caso, podemos ajustar el punto inicial, la tasa de aprendizaje y el número de iteraciones para ver cómo el algoritmo encuentra el mínimo."),
      br(),
      
      # Teoría más detallada
      tags$h4(" ¿ Y cómo Funciona? "),
      p("1. Empieza en un punto cualquiera."),
      p("2. Calcula el gradiente, que es la pendiente en ese punto."),
      p("3. Se mueve en la dirección opuesta al gradiente."),
      p("4. Repite este proceso para mejorar el valor."),
      p("Usa los controles para experimentar con diferentes puntos iniciales, tasas de aprendizaje y número de iteraciones."),
      
      br(),
      h4("Parámetros"),
      sliderInput("punto_inicial", "Punto inicial:", min = -6, max = 6, value = -5, step = 0.5),
      sliderInput("tasa_aprendizaje", "Tasa de aprendizaje:", min = 0.01, max = 1, value = 0.1, step = 0.01),
      sliderInput("iteraciones", "Número de iteraciones:", min = 1, max = 50, value = 30, step = 1),
      
      actionButton("calcular", "Calcular")
    ),
    
    mainPanel(
      h3("Gráfico del Descenso de Gradiente"),
      plotOutput("grafico"),
      br(),
      h4("Iteraciones de Descenso de Gradiente"),
      tableOutput("tabla")
    )
  )
)

# Lógica del servidor
server <- function(input, output) {
  resultados <- reactive({
    input$calcular
    isolate({
      punto_inicial <- input$punto_inicial
      tasa_aprendizaje <- input$tasa_aprendizaje
      iteraciones <- input$iteraciones
      
      historial <- descenso_gradiente(punto_inicial, tasa_aprendizaje, iteraciones)
      data.frame(
        Iteración = 0:iteraciones,
        Punto = historial,
        Valor = objetivo(historial)
      )
    })
  })
  
  output$grafico <- renderPlot({
    datos <- resultados()
    x_vals <- seq(-6, 6, length.out = 500)
    
    plot(
      x_vals, objetivo(x_vals), type = "l", col = "blue", lwd = 2,
      xlab = "x", ylab = "f(x)", main = "Descenso de Gradiente"
    )
    
    points(datos$Punto, datos$Valor, col = "red", pch = 19)
    lines(datos$Punto, datos$Valor, col = "red", lwd = 1, lty = 2)
    
    legend("topright", legend = c("Función Objetivo", "Iteraciones"), 
           col = c("blue", "red"), lty = c(1, 2), pch = c(NA, 19), lwd = c(2, 1))
  })
  
  output$tabla <- renderTable({
    resultados()
  })
}

# Ejecutar la aplicación
shinyApp(ui = ui, server = server)
