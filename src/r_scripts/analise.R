# ===== ANALISE.R =====

suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(readr))

# ===== Funções utilitárias =====

formatar_valor <- function(v, sufixo = "") {
  if (is.na(v)) return("—")
  if (is.numeric(v)) return(sprintf("%.2f%s", v, sufixo))
  return(as.character(v))
}

exibir_cabecalho_tabela <- function() {
  cat("\n===== 🌱 DADOS DE CULTIVOS REGISTRADOS =====\n\n")
  cat(sprintf(
    "%-6s  %-30s  %-10s  %8s  %10s  %6s  %6s  %-10s  %12s  %12s  %14s\n",
    "TIPO", "DESCRIÇÃO", "ÁREA", "LARGURA", "COMPRIM.", "BASE", "ALTURA",
    "INSUMO", "QTD. INSUMO", "ÁREA TOTAL", "INSUMO TOTAL"
  ))
  cat(rep("─", 128), "\n", sep = "")
}

exibir_linha_tabela <- function(row) {
  cat(sprintf(
    "%-6s  %-30s  %-10s  %8s  %10s  %6s  %6s  %-10s  %12s  %12s  %14s\n",
    row$tipo,
    substr(row$descricao, 1, 30),
    formatar_valor(row$formato_area),
    formatar_valor(row$largura, " m"),
    formatar_valor(row$comprimento, " m"),
    formatar_valor(row$base, " m"),
    formatar_valor(row$altura, " m"),
    row$insumo,
    formatar_valor(row$quantidade_insumo, " kg"),
    formatar_valor(row$total_area, " m²"),
    formatar_valor(row$total_insumo, " kg")
  ))
}

exibir_estatisticas <- function(df, tipo) {
  media_area <- mean(df$total_area, na.rm = TRUE)
  desvio_area <- sd(df$total_area, na.rm = TRUE)

  media_insumo <- mean(df$total_insumo, na.rm = TRUE)
  desvio_insumo <- sd(df$total_insumo, na.rm = TRUE)

  cat(sprintf("🌾 %s\n", toupper(tipo)))
  cat(sprintf("📏  Média da área plantada:    %.2f m²\n", media_area))
  cat(sprintf("📐  Desvio padrão da área:     %.2f m²\n", desvio_area))
  cat(sprintf("🧪  Média do insumo total:     %.2f kg\n", media_insumo))
  cat(sprintf("📉  Desvio padrão do insumo:   %.2f kg\n\n", desvio_insumo))
}

# ===== Leitura dos dados =====
dados <- read_csv("src/../data/culturas.csv", show_col_types = FALSE)

# ===== Exibição da Tabela =====
exibir_cabecalho_tabela()
for (i in 1:nrow(dados)) {
  exibir_linha_tabela(dados[i, ])
}

# ===== Estatísticas por Tipo =====
cat("\n\n===== 📊 ANALISE ESTATISTICA POR TIPO =====\n\n")

tipos <- unique(dados$tipo)
for (tipo in tipos) {
  grupo <- filter(dados, tipo == !!tipo)
  exibir_estatisticas(grupo, tipo)
}
