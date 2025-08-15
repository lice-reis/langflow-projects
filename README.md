# Langflow Custom Components

Este repositório contém componentes customizados para o Langflow, uma plataforma de desenvolvimento de fluxos de IA.

## Componente Disponível

### Save File Component

O componente **Save File** permite salvar arquivos de diferentes formatos (JSON, CSV, TXT) durante a execução de fluxos no Langflow.

#### Características
- Suporte para múltiplos formatos de arquivo
- Configuração flexível de caminhos de saída
- Integração nativa com o Langflow
- Tratamento de erros robusto

#### Arquivos do Componente
- `save_file_new.py` - **Componente principal** (versão atualizada e otimizada)
- `CHANGELOG.md` - Histórico de mudanças

#### Como Usar
1. Copie o arquivo `save_file_new.py` para a pasta `Components/Custom/` do seu projeto Langflow
2. Reinicie o Langflow
3. O componente aparecerá na lista de componentes customizados

## Instalação

```bash
git clone https://github.com/lice-reis/langflow-projects.git
cd langflow-projects
```

## Estrutura do Projeto

```
Components/
└── Custom/
    └── save-file/
        ├── save_file_new.py    # Componente principal
        └── CHANGELOG.md        # Histórico de versões
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias e novos componentes!

## Licença

Este projeto está sob a licença MIT.
