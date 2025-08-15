# Save File Component for Langflow

Um componente customizado para o Langflow que permite salvar arquivos de diferentes formatos durante a execução de fluxos.

## Características

- ✅ Suporte para múltiplos formatos de arquivo (JSON, CSV, TXT)
- ✅ Configuração flexível de caminhos de saída
- ✅ Integração nativa com o Langflow
- ✅ Tratamento de erros robusto
- ✅ Interface limpa e intuitiva

## Arquivos do Componente

- `save_file_new.py` - **Componente principal** (versão atualizada e otimizada)
- `CHANGELOG.md` - Histórico de mudanças e versões

## Como Usar

1. **Instalação**: Copie o arquivo `save_file_new.py` para a pasta `Components/Custom/` do seu projeto Langflow
2. **Reiniciar**: Reinicie o Langflow para carregar o novo componente
3. **Usar**: O componente aparecerá na lista de componentes customizados

## Configuração

O componente aceita os seguintes parâmetros:
- **File Path**: Caminho onde o arquivo será salvo
- **File Name**: Nome do arquivo (com extensão)
- **Content**: Conteúdo a ser salvo no arquivo
- **File Format**: Formato do arquivo (JSON, CSV, TXT)

## Exemplo de Uso

```python
# O componente salva automaticamente o conteúdo no formato especificado
# e retorna o caminho completo do arquivo salvo
```

## Compatibilidade

- Langflow versão 0.5.0+
- Python 3.8+
- Sistemas: Windows, macOS, Linux

## Licença

Este componente está sob a licença MIT.
