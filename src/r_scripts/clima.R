# ===== PACOTES =====
if (!require("httr")) install.packages("httr", dependencies = TRUE)
if (!require("jsonlite")) install.packages("jsonlite", dependencies = TRUE)

library(httr)
library(jsonlite)

# ===== FUNCAO DE LOG =====
log_erro <- function(mensagem) {
  dir.create("logs", showWarnings = FALSE)
  cat(sprintf("[%s] %s\n", Sys.time(), mensagem), file = "logs/clima.log", append = TRUE)
}

# ===== .env E API KEY =====
env_path <- file.path(getwd(), ".env")

if (!file.exists(env_path)) {
  msg <- "Arquivo .env nao encontrado. Mais informações em README.md."
  cat("⚠️ ", msg, "\n")
  log_erro(msg)
  quit()
}

env_lines <- readLines(env_path)
api_line <- grep("^OWM_API_KEY=", env_lines, value = TRUE)

if (length(api_line) == 0) {
  msg <- "Variavel OWM_API_KEY nao encontrada no .env."
  cat("⚠️ ", msg, "\n")
  log_erro(msg)
  quit()
}

api_key <- trimws(sub("OWM_API_KEY=", "", api_line))

if (api_key == "") {
  msg <- "Chave da API esta vazia."
  cat("⚠️ ", msg, "\n")
  log_erro(msg)
  quit()
}

# ===== LOCALIZACAO FIXA: SAO PAULO, BRASIL =====
cidade <- "Sao Paulo"
pais <- "BR"

# ===== MONTAGEM DA URL =====
url <- sprintf(
  "https://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s&units=metric&lang=pt_br",
  URLencode(cidade), pais, api_key
)

# ===== REQUISICAO =====
res_clima <- tryCatch(GET(url), error = function(e) {
  msg <- paste("Erro na requisicao:", e$message)
  cat("❌", msg, "\n")
  log_erro(paste(msg, "\nURL:", url))
  return(NULL)
})

if (is.null(res_clima)) {
  msg <- "Nao foi possivel obter a previsao do tempo (requisicao falhou)."
  cat("⚠️ ", msg, "\n")
  log_erro(msg)
  quit()
}

codigo <- status_code(res_clima)

if (codigo != 200) {
  corpo <- content(res_clima, "text", encoding = "UTF-8")
  msg <- sprintf("Falha na requisicao: status %d\nCorpo: %s", codigo, corpo)
  cat("⚠️ ", msg, "\n")
  log_erro(paste(msg, "\nURL:", url))
  quit()
}

# ===== EXTRACAO E EXIBICAO DE DADOS =====
dados_raw <- content(res_clima, "text", encoding = "UTF-8")
dados <- fromJSON(dados_raw, simplifyVector = FALSE)

if (!is.list(dados) || !"weather" %in% names(dados)) {
  msg <- paste("Resposta inesperada da API:\n", dados_raw)
  cat("⚠️ ", msg, "\n")
  log_erro(msg)
  quit()
}

nome_cidade <- dados$name
descricao <- dados$weather[[1]]$description
temperatura <- dados$main$temp
umidade <- dados$main$humidity
vento <- dados$wind$speed

cat("🌤️  PREVISAO DO TEMPO\n")
cat(sprintf("📍 %s\n", nome_cidade))
cat(sprintf("☁️  %s\n", toupper(descricao)))
cat(sprintf("🌡️  %.1f °C    💧 %d%%    💨 %.1f m/s\n", temperatura, umidade, vento))
