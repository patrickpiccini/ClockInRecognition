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
absl-py==1.3.0
astunparse==1.6.3
autopep8==2.0.0
cachetools==5.2.0
certifi==2022.9.24
charset-normalizer==2.1.1
click==8.1.3
cmake==3.24.1.1
cmake-build-extension==0.5.1
colorama==0.4.6
contourpy==1.0.6
cycler==0.11.0
DateTime==4.7
dlib==19.24.0
face-recognition==1.3.0
face-recognition-models==0.3.0
flatbuffers==22.10.26
fonttools==4.38.0
gast==0.4.0
gitdb==4.0.9
GitPython==3.1.29
google-auth==2.14.0
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
grpcio==1.50.0
h5py==3.7.0
idna==3.4
imutils==0.5.4
joblib==1.2.0
keras==2.10.0
Keras-Preprocessing==1.1.2
kiwisolver==1.4.4
libclang==14.0.6
Markdown==3.4.1
MarkupSafe==2.1.1
matplotlib==3.6.2
ninja==1.10.2.4
numpy==1.23.1
oauthlib==3.2.2
opencv-python==4.6.0.66
opt-einsum==3.3.0
packaging==21.3
Pillow==9.2.0
protobuf==3.19.6
psycopg2==2.9.5
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycodestyle==2.9.1
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2022.5
regex==2022.9.13
requests==2.28.1
requests-oauthlib==1.3.1
rsa==4.9
scikit-learn==1.1.3
scipy==1.9.3
setuptools-scm==7.0.5
six==1.16.0
smmap==5.0.0
tensorboard==2.10.1
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow==2.10.0
tensorflow-estimator==2.10.0
tensorflow-io-gcs-filesystem==0.27.0
termcolor==2.1.0
threadpoolctl==3.1.0
tomli==2.0.1
typing_extensions==4.4.0
urllib3==1.26.12
Werkzeug==2.2.2
wrapt==1.14.1
zope.interface==5.5.0

```

#### Diagrama
![Diagrama](https://user-images.githubusercontent.com/66441004/200970468-5b2fa0c9-700a-42bd-b789-84ea021e5210.png)

