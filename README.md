### Informações
Repositório criado para a Atividade Avaliativa - Projeto Computer Vision Full.  
Disciplina: Computação Gráfica  
Professor: Marcos Roberto dos Santos  
Alunos: Eduardo Bido e Patrick Piccini

### Projeto
O projeto tem como finalidade automatizar o "bater ponto" dos funcionários por reconhecimento facial, reconhecer se este está usando capacete ou não e se o trabalhador com determinada cor de capacete tem acesso a determinado local.

### Requisitos

* ✅ Possui um HaarCascade - O HaarCascace está sendo utilizado no reconhecimendo do capacete.
<img src = 'https://github.com/patrickpiccini/ClockInRecognition/blob/main/prints/07%20-%20Detec%C3%A7%C3%A3o%20de%20capacete%20por%20Haar%20Cascate.png' width='600'/>

* ✅ Gerar algum tipo de log - O registro de ponto está sendo considerado como log e este está sendo salvo no banco de dados.
<img src = 'https://github.com/patrickpiccini/ClockInRecognition/blob/main/prints/03%20-%20Registro%20de%20log%20do%20cadastro%20de%20usuario.png' width='600'/>
<img src = 'https://github.com/patrickpiccini/ClockInRecognition/blob/main/prints/05%20-%20Registro%20de%20Log%20no%20postgres.png' width='600'/>

* ✅ Possuir identificação facial - Está sendo usado no momento de bater o ponto, HaarCascade e TensorFlow.
<img src = 'https://github.com/patrickpiccini/ClockInRecognition/blob/main/prints/06%20-%20detec%C3%A7%C3%A3o%20de%20faces%20registradas.png' width='400'/>


* ✅ Aplicar técnicas de processamento de imagens como redimensionamento, recorte e mudança de cores - É recortado o capacete para reconecer a cor posteriormente
* ✅ Incluir uma skill referente a seleção a seleção de objetos por cores, o qual deve executar alguma ação pré-definida. - É reconhecia a cor do recorte, e verificado se tem o acesso ao local
* ✅ Aplicar técnicas de binarização e detecção de bordas, aplicando correção morfológica nas imagens. - Para deconhecer a Cor é feito a binarização para a detecção da borda do objeto capacete
<img src = 'https://github.com/patrickpiccini/ClockInRecognition/blob/main/prints/10%20-%20Registro%20de%20Funcionario%20n%C3%A3o%20autorizado.png' width='600'/>

### Biblioteca Usadas
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

### Diagra
<img src = 'https://user-images.githubusercontent.com/66441004/201454398-6b1950eb-6250-4a8e-9b7e-4d0b6902e352.png' width='800'/>



