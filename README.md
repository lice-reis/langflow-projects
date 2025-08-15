# Langflow Custom Components

Este repositório contém componentes customizados para o Langflow, uma plataforma de desenvolvimento de fluxos de IA.

## Componentes Disponíveis

### Save File Component

O componente **Save File** permite salvar arquivos de diferentes formatos (JSON, CSV, TXT) durante a execução de fluxos no Langflow.

#### Características
- Suporte para múltiplos formatos de arquivo
- Configuração flexível de caminhos de saída
- Integração nativa com o Langflow
- Tratamento de erros robusto

#### Arquivos do Componente
- `file.py` - Implementação principal do componente
- `save_file_new.py` - Versão atualizada do componente
- `save_file_old.py` - Versão anterior para referência
- `test_component.py` - Testes do componente
- `test.json` - Arquivo de teste
- `CHANGELOG.md` - Histórico de mudanças

#### Como Usar
1. Copie os arquivos do componente para a pasta `Components/Custom/` do seu projeto Langflow
2. Reinicie o Langflow
3. O componente aparecerá na lista de componentes customizados

## Instalação

```bash
git clone <seu-repositorio>
cd "Langflow Project"
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias e novos componentes!

## Licença

Este projeto está sob a licença MIT.
