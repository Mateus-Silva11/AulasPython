from pessoa_db import listar_todos
from pessoa_coverte import converter_tabela_dicionario
from pessoa_exeporta import exportar_txt

lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)