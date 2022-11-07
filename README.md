### Informações
Repositório criado para a Atividade Avaliativa - Projeto Computer Vision Full.  
Disciplina: Computação Gráfica  
Professor: Marcos Roberto dos Santos  
Alunos: Eduardo Bido e Patrick Piccini

### Projeto
O projeto tem como finalidade automatizar o "bater ponto" dos funcionários por reconhecimento facial e também reconhecer se este está usando capacete ou não.

### Requisitos
* Aplicar técnicas de processamento de imagens como redimensionamento, recorte e mudança de cores - Ao registrar o ponto é feito um resize no frame original para prosseguir com a técnica de reconhecimento facial. ✅
* Possui um HaarCascade - O HaarCascace está sendo utilizado no reconhecimendo do capacete. ✅
* Gerar algum tipo de log - O registro de ponto está sendo considerado como log e este está sendo salvo no banco de dados. ✅
* Possuir identificação facial - Está sendo usado na hora de registrar uma nova pessoa ou no momento de bater o ponto. ✅
* Aplicar técnicas de binarização e detecção de bordas, aplicando correção morfológica nas imagens.
* Incluir uma skill referente a seleção a seleção de objetos por cores, o qual deve executar alguma ação pré-definida.

#### Biblioteca Usadas
```
click==8.1.3
cmake==3.24.1.1
cmake-build-extension==0.5.1
colorama==0.4.6
DateTime==4.7
dlib==19.24.0
face-recognition==1.3.0
face-recognition-models==0.3.0
gitdb==4.0.9
GitPython==3.1.29
ninja==1.10.2.4
numpy==1.23.1
opencv-python==4.6.0.66
packaging==21.3 Pillow==9.2.0
psycopg2==2.9.5
pyparsing==3.0.9
pytz==2022.5
regex==2022.9.13
setuptools-scm==7.0.5
smmap==5.0.0
tomli==2.0.1
typing_extensions==4.4.0
zope.interface==5.5.0
```

#### Diagrama
![Diagrama](https://user-images.githubusercontent.com/58514930/200431703-620b4c0f-db91-4f6f-8e34-68583c4dc623.png)
