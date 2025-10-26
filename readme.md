# 📸 Screenshot to Gemini Analyzer

<div align="center">

### 🌍 Language / Idioma

[![English](https://img.shields.io/badge/🇺🇸-English-blue?style=for-the-badge)](#english) [![Português](https://img.shields.io/badge/🇧🇷-Português-green?style=for-the-badge)](#português)

---

</div>

## English

A Python application that automatically captures screenshots and uses Google Gemini AI to analyze multiple-choice questions, sending results to a Google Chat webhook.

### 📋 Table of Contents

- [🚀 Features](#Features)
- [📋 Prerequisites](#prerequisites)
- [🛠️ Installation](#installation)
- [⚙️ Configuration](#configuration)
- [🎮 How to Use](#how-to-use)
- [🥷 Stealth Mode](#stealth-mode)
- [📊 Response Format](#response-format)
- [📁 Project Structure](#project-structure)
- [📝 Logs](#logs)
- [🔧 Customization](#customization)
- [⚠️ Limitations](#limitations)
- [📄 License](#license)

### Features

- **Automatic screenshot capture** via keyboard shortcuts
- **Intelligent analysis** of multiple-choice questions using Gemini AI
- **Automatic result sending** to webhook
- **Shortcut-based interface** for easy use
- **Complete logging** of all operations

### Prerequisites

- Python 3.8+
- Google Cloud account with Gemini AI enabled
- Configured webhook (Google Chat)

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd screenshot-gemini-analyzer
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure the configuration file:**
   - Rename `config/config.example.json` to `config/config.json`
   - Fill in the necessary configurations

### Configuration

#### `config/config.json` file:

```json
{
  "webhook": "your_webhook_url_here",
  "google_genai_secret_file": "path/to/your/credentials.json",
  "gemini_model": "gemini-2.5-flash-lite",
  "shutdown_application_keys": ["0"],
  "callback_screenshot_to_gemini_keys": ["up", "down", "left", "right", "alt", "f9"]
}
```

#### Google Cloud Configuration:

1. Access [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gemini API
4. Create a service account and download the JSON credentials file
5. Put the file path in the `google_genai_secret_file` field

#### Webhook Configuration:

- **Google Chat:** Create a webhook in your Google Chat

### How to Use

1. **Start the application:**
```bash
python main.py
```

2. **Available shortcuts:**
   - **📸 Capture and analyze:** `↑`, `↓`, `←`, `→`, `Alt`, `F9`
   - **🔴 Close application:** `0`

3. **Usage flow:**
   - Press one of the capture shortcuts
   - The screenshot will be captured automatically
   - The image will be sent to Gemini AI
   - The result will be sent to the configured webhook

### Stealth Mode

To use the application discreetly, you can generate an executable that runs in the background without visible windows.

#### Generating the Stealth Executable:

1. **Install PyInstaller:**
```bash
pip install pyinstaller
```

2. **Prepare necessary files:**
   - Place an `ico.ico` file in the project root (executable icon)
   - Make sure the `config/` folder is properly configured

3. **Run the compilation command:**
```bash
pyinstaller --onefile --noconsole --windowed --name "Microsoft Security Health Service" --icon "ico.ico" --add-data "config;config" main.py
```

#### Parameter explanation:

- `--onefile`: Generates a single executable file
- `--noconsole`: Removes the console window (silent execution)
- `--windowed`: Runs in window mode (no terminal)
- `--name "Microsoft Security Health Service"`: Executable name (disguised as Windows service)
- `--icon "ico.ico"`: Sets the executable icon
- `--add-data "config;config"`: Includes the config folder in the executable

#### After compilation:

1. The executable will be generated in the `dist/` folder
2. The file will be named `Microsoft Security Health Service.exe`
3. Can be run directly without Python installation
4. Runs completely in the background

#### Stealth Mode Tips:

- **Disguised name:** The executable uses a name that looks like a legitimate Windows service
- **No visual interface:** Doesn't open visible windows or consoles
- **Discrete shortcuts:** Use less obvious key combinations
- **Silent logs:** Logs are saved to file, not displayed on screen

#### Stealth usage example:

```json
{
  "callback_screenshot_to_gemini_keys": ["ctrl+shift+f12", "alt+f10"],
  "shutdown_application_keys": ["ctrl+shift+esc"]
}
```

#### Legal Notice:

This mode is intended for personal and educational use

### Response Format

Gemini AI returns analyses in the following format:

```
QUESTION NUMBER: [question number]
CORRECT ANSWER: [alternative + alternative text]
```

### Project Structure

```
├── main.py                           # Main file
├── config/
│   └── config.json                   # Application configurations
│   └── gen-lang-client.json          # Google token
├── utils/
│   ├── listener_keyboard.py          # Keyboard shortcut manager
│   ├── screenshot_clipboard.py       # Screenshot capture
│   ├── logger.py                     # Logging system
│   ├── gemini_services.py            # Gemini AI integration
│   ├── send_msg_to_webhook.py        # Webhook sending
│   └── load_json_config.py           # Configuration loading
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

### Logs

The application generates detailed logs in the `log.log` file, including:
- Application initialization
- Screenshot captures
- Gemini AI interactions
- Webhook sends
- Errors and exceptions

### Customization

#### Available Gemini Models:
- `gemini-2.5-flash-lite` (default)
- `gemini-2.5-flash`
- `gemini-2.5-pro`

#### Custom Shortcuts:
Edit the `config.json` file to customize shortcuts:

```json
{
  "callback_screenshot_to_gemini_keys": ["f1", "f2", "ctrl+s"],
  "shutdown_application_keys": ["esc", "ctrl+q"]
}
```

### Limitations

- Requires internet connection
- Dependent on captured image quality

### License

This project is under the MIT license. See the `LICENSE` file for more details.

---

## Português

Um aplicativo Python que captura screenshots automaticamente e utiliza o Google Gemini AI para analisar questões de múltipla escolha, enviando os resultados para um webhook Google Chat.

### Índice

- [🚀 Funcionalidades](#funcionalidades)
- [📋 Pré-requisitos](#pré-requisitos)
- [🛠️ Instalação](#instalação)
- [⚙️ Configuração](#configuração)
- [🎮 Como Usar](#como-usar)
- [🥷 Modo Furtivo](#modo-furtivo)
- [📊 Formato de Resposta](#formato-de-resposta)
- [📁 Estrutura do Projeto](#estrutura-do-projeto)
- [📝 Logs](#logs)
- [🔧 Personalização](#personalização)
- [⚠️ Limitações](#limitações)
- [📄 Licença](#licença)

### Funcionalidades

- **Captura automática de screenshot** via atalhos de teclado
- **Análise inteligente** de questões de múltipla escolha usando Gemini AI
- **Envio automático** de resultados para webhook
- **Interface por atalhos** para facilitar o uso
- **Logging completo** de todas as operações

### Pré-requisitos

- Python 3.8+
- Conta Google Cloud com Gemini AI habilitado
- Webhook configurado (Google Chat)

### Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd screenshot-gemini-analyzer
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure o arquivo de configuração:**
   - Renomeie `config/config.example.json` para `config/config.json`
   - Preencha as configurações necessárias

### Configuração

#### Arquivo `config/config.json`:

```json
{
  "webhook": "sua_url_do_webhook_aqui",
  "google_genai_secret_file": "caminho/para/seu/arquivo/credenciais.json",
  "gemini_model": "gemini-2.5-flash-lite",
  "shutdown_application_keys": ["0"],
  "callback_screenshot_to_gemini_keys": ["up", "down", "left", "right", "alt", "f9"]
}
```

#### Configuração do Google Cloud:

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Habilite a API do Gemini
4. Crie uma conta de serviço e baixe o arquivo JSON de credenciais
5. Coloque o caminho do arquivo no campo `google_genai_secret_file`

#### Configuração do Webhook:

- **Google Chat:** Crie um webhook no seu chat Google Chat

### Como Usar

1. **Inicie a aplicação:**
```bash
python main.py
```

2. **Atalhos disponíveis:**
   - **�� Capturar e analisar:** `↑`, `↓`, `←`, `→`, `Alt`, `F9`
   - **🔴 Finalizar aplicação:** `0`

3. **Fluxo de uso:**
   - Pressione um dos atalhos de captura
   - O screenshot será capturado automaticamente
   - A imagem será enviada para o Gemini AI
   - O resultado será enviado para o webhook configurado

### Modo Furtivo

Para usar a aplicação de forma discreta, você pode gerar um executável que roda em segundo plano sem janelas visíveis.

#### Gerando o Executável Furtivo:

1. **Instale o PyInstaller:**
```bash
pip install pyinstaller
```

2. **Prepare os arquivos necessários:**
   - Coloque um arquivo `ico.ico` na raiz do projeto (ícone do executável)
   - Certifique-se de que a pasta `config/` está configurada corretamente

3. **Execute o comando de compilação:**
```bash
pyinstaller --onefile --noconsole --windowed --name "Microsoft Security Health Service" --icon "ico.ico" --add-data "config;config" main.py
```

#### Explicação dos parâmetros:

- `--onefile`: Gera um único arquivo executável
- `--noconsole`: Remove a janela do console (execução silenciosa)
- `--windowed`: Executa em modo janela (sem terminal)
- `--name "Microsoft Security Health Service"`: Nome do executável (disfarçado como serviço do Windows)
- `--icon "ico.ico"`: Define o ícone do executável
- `--add-data "config;config"`: Inclui a pasta config no executável

#### Após a compilação:

1. O executável será gerado na pasta `dist/`
2. O arquivo se chamará `Microsoft Security Health Service.exe`
3. Pode ser executado diretamente sem instalação do Python
4. Roda completamente em segundo plano

#### Dicas para Modo Furtivo:

- **Nome disfarçado:** O executável usa um nome que parece um serviço legítimo do Windows
- **Sem interface visual:** Não abre janelas ou consoles visíveis
- **Atalhos discretos:** Use combinações de teclas menos óbvias
- **Logs silenciosos:** Os logs ficam salvos em arquivo, não na tela

#### Exemplo de uso furtivo:

```json
{
  "callback_screenshot_to_gemini_keys": ["ctrl+shift+f12", "alt+f10"],
  "shutdown_application_keys": ["ctrl+shift+esc"]
}
```

#### Aviso Legal:

Este modo é destinado para uso pessoal e educacional

### Formato de Resposta

O Gemini AI retorna as análises no seguinte formato:

```
NUMERO DA QUESTÃO: [número da questão]
RESPOSTA CORRETA: [alternativa + texto da alternativa]
```

### Estrutura do Projeto

```
├── main.py                           # Arquivo principal
├── config/
│   └── config.json                   # Configurações da aplicação
│   └── gen-lang-client.json          # Google token
├── utils/
│   ├── listener_keyboard.py          # Gerenciador de atalhos de teclado
│   ├── screenshot_clipboard.py       # Captura de screenshot
│   ├── logger.py                     # Sistema de logging
│   ├── gemini_services.py            # Integração com Gemini AI
│   ├── send_msg_to_webhook.py        # Envio para webhook
│   └── load_json_config.py           # Carregamento de configurações
├── requirements.txt                  # Dependências Python
└── README.md                         # Este arquivo
```

### Logs

A aplicação gera logs detalhados no arquivo `log.log`, incluindo:
- Inicialização da aplicação
- Capturas de screenshot
- Interações com o Gemini AI
- Envios para webhook
- Erros e exceções

### Personalização

#### Modelos Gemini Disponíveis:
- `gemini-2.5-flash-lite` (padrão)
- `gemini-2.5-flash`
- `gemini-2.5-pro`

#### Atalhos Personalizados:
Edite o arquivo `config.json` para personalizar os atalhos:

```json
{
  "callback_screenshot_to_gemini_keys": ["f1", "f2", "ctrl+s"],
  "shutdown_application_keys": ["esc", "ctrl+q"]
}
```

### Limitações

- Requer conexão com internet
- Dependente da qualidade da imagem capturada

### Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!**

**⭐ If this project was useful to you, consider giving the repository a star!**

</div>