# Generated by Django 5.1.3 on 2024-12-20 11:20

import app_alumnalia.modelos.modelFormacion
import app_alumnalia.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambito',
            fields=[
                ('pk_amb', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Ambito')),
                ('desc_amb', models.CharField(max_length=200, verbose_name='Descripcion del Ambito')),
            ],
            options={
                'db_table': 'Ambito',
            },
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('pk_cal', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de Calendario')),
                ('dat_ini_cal', models.DateField(verbose_name='Fecha de inicio del curso')),
                ('dat_fin_cal', models.DateField(verbose_name='Fecha de fin del curso')),
                ('nom_grup_cal', models.CharField(max_length=30, verbose_name='Numero de grupo asignado en el calendario')),
            ],
            options={
                'db_table': 'Calendario',
            },
        ),
        migrations.CreateModel(
            name='Comarca',
            fields=[
                ('pk_com', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='id de Comarca')),
                ('nom_com', models.CharField(max_length=30, verbose_name='nombre de la Comarca')),
            ],
            options={
                'db_table': 'Comarca',
            },
        ),
        migrations.CreateModel(
            name='Dat_Per',
            fields=[
                ('pk_per', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='id de la Dat_Per')),
                ('nom_per', models.CharField(max_length=150, verbose_name='Nombre')),
                ('dni_per', models.CharField(max_length=15, unique=True, validators=[app_alumnalia.models.validar_dni], verbose_name='DNI/NIE')),
                ('fn_per', models.DateField(verbose_name='Fecha de nacimiento')),
                ('fn_per_enc', models.CharField(default='', max_length=15, verbose_name='Fecha de nacimiento encriptada')),
                ('cn_per', models.CharField(max_length=150, verbose_name='Nacionalidad')),
                ('tel_per', models.IntegerField(validators=[app_alumnalia.models.validar_longitud_nueve], verbose_name='Teléfono')),
                ('tel_per_enc', models.CharField(default='', max_length=10, verbose_name='Teléfono encriptada')),
                ('email_per', models.EmailField(max_length=254, verbose_name='Email')),
                ('dir_per', models.CharField(max_length=150, verbose_name='Dirección')),
                ('sex_per', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Mujer'), ('2', 'Hombre'), ('3', 'Prefiero no especificar'), ('4', 'Otro')], default='', max_length=1, verbose_name='Género de la persona')),
                ('uso_datos_per', models.BooleanField(default=False, verbose_name='Fines de gestión académica y administrativa')),
                ('term_per', models.BooleanField(default=False, verbose_name='Términos y condiciones')),
                ('noti_per', models.BooleanField(default=False, verbose_name='Notificaciones de oportunidades formativas')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=30, verbose_name='Contraseña')),
            ],
            options={
                'db_table': 'Dat_Per',
            },
        ),
        migrations.CreateModel(
            name='Denominacion',
            fields=[
                ('pk_deno', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Denominacion')),
                ('desc_den', models.CharField(max_length=200, verbose_name='Descripcion de la Denominacion')),
            ],
            options={
                'db_table': 'Denominacion',
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('pk_esc', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Entidad Formadora')),
                ('nom_esc', models.CharField(max_length=44, verbose_name='nombre de Entidad Formadora')),
                ('email_esc', models.EmailField(max_length=254, verbose_name='correo de la entidad')),
                ('nif_esc', models.CharField(max_length=20, verbose_name='NIF de Entidad Formadora')),
                ('web_esc', models.CharField(max_length=100, verbose_name='link de la web de Entidad Formadora')),
                ('tel_esc', models.CharField(max_length=15, validators=[app_alumnalia.modelos.modelFormacion.validar_longitud_nueve], verbose_name='telefono de Entidad Formadora')),
            ],
            options={
                'db_table': 'Escuela',
            },
        ),
        migrations.CreateModel(
            name='Estudio_Profesion',
            fields=[
                ('pk_est_pro', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Estudio Profecional')),
                ('desc_est_pro', models.CharField(max_length=220, verbose_name='Descripcion de la Estudio Profesional')),
            ],
            options={
                'db_table': 'Estudio_Profesional',
            },
        ),
        migrations.CreateModel(
            name='Familia_Profesion',
            fields=[
                ('pk_fm_pro', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Entidad Formadora')),
                ('desc_fm_pro', models.CharField(max_length=200, verbose_name='Descripcion de la Familia Profesional')),
            ],
            options={
                'db_table': 'Familia_Profesional',
            },
        ),
        migrations.CreateModel(
            name='MisDirecciones',
            fields=[
                ('pk_com', models.AutoField(primary_key=True, serialize=False)),
                ('nom_com', models.CharField(max_length=30, verbose_name='nombre de la Comarca')),
                ('pk_pro', models.SmallIntegerField(verbose_name='id de Provincias')),
                ('nom_pro', models.CharField(max_length=30, verbose_name='nombre de la Provincia')),
                ('pk_mun', models.IntegerField(verbose_name='id de Municipios')),
                ('nom_mun', models.CharField(max_length=30, verbose_name='nombre de la Municipios')),
            ],
            options={
                'db_table': 'MisDirecciones',
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('pk_pro', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='id de Provincias')),
                ('nom_pro', models.CharField(max_length=30, verbose_name='nombre de la Provincia')),
            ],
            options={
                'db_table': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('pk_tip_user', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de tip de usurio')),
                ('nom_tip_user', models.CharField(max_length=10, verbose_name='Descripcion del tipo de usuario')),
                ('per_tip_user', models.SmallIntegerField(verbose_name='permiso del tipo de usuario')),
            ],
            options={
                'db_table': 'Tipo_Usuario',
            },
        ),
        migrations.CreateModel(
            name='TipoVia',
            fields=[
                ('pk_via', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='id de Tipo de Via')),
                ('nom_via', models.CharField(max_length=100, verbose_name='Tipo de via')),
            ],
            options={
                'db_table': 'TipoVia',
            },
        ),
        migrations.CreateModel(
            name='Cusrso',
            fields=[
                ('pk_cal', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Curso')),
                ('idt_ent_for', models.IntegerField(verbose_name='identificador de la Entiad Formadora')),
                ('area_prof_ent_for', models.CharField(max_length=44, verbose_name='Area Porfecional de Entidad Formadora')),
                ('horas_ent_for', models.TimeField(blank=True, null=True, verbose_name='horas de la Entidad Formadora')),
                ('mod_cur', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Presencial'), ('2', 'En línea'), ('3', 'Mixta')], default='', max_length=1, verbose_name='Modalidad de estudio')),
                ('fk_amb_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ambito', to='app_alumnalia.ambito', verbose_name='Ambito de Entidad Formadora')),
                ('fk_den_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Denomincion', to='app_alumnalia.denominacion')),
                ('fk_fam_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cusrso', to='app_alumnalia.familia_profesion')),
            ],
            options={
                'db_table': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='Inf_Prof',
            fields=[
                ('pk_inf_pro', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='id de la Información Profesional')),
                ('tit_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Sin estudios'), ('2', 'Primaria'), ('3', 'Secundaria'), ('4', 'Bachillerato'), ('5', 'Técnico/a'), ('6', 'Grado universitario'), ('7', 'Máster'), ('8', 'Doctorado'), ('9', 'Otros')], default='', max_length=1, verbose_name='Título académico más alto obtenido')),
                ('tit_esp_inf_pro', models.CharField(max_length=15, verbose_name='Especifique título')),
                ('esp_inf_pro', models.CharField(max_length=15, verbose_name='¿En qué área está tu especialización principal?')),
                ('exp_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Menos de 1 año'), ('2', 'De 1 a 3 años'), ('3', 'De 4 a 6 años'), ('4', 'Más de 6 años')], default='', max_length=1, verbose_name='¿Cuántos años de experiencia tienes como formador/a?')),
                ('for_imp_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Formación profesional'), ('2', 'Formación universitaria'), ('3', 'Formación empresarial'), ('4', 'Cursos en línea'), ('5', 'Otros')], default='', max_length=1, verbose_name='Qué tipo de formación has impartido')),
                ('for_imp_esp_inf_pro', models.CharField(max_length=255, verbose_name='Especifique que formación ha impartido')),
                ('cv_adj_inf_pro', models.FileField(blank=True, null=True, upload_to='pdfs/', verbose_name='Adjunta tu currículum en formato PDF.')),
                ('cert_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Sí'), ('2', 'No')], default='', max_length=1, verbose_name='¿Tienes alguna certificación docente?')),
                ('cert_esp_inf_pro', models.CharField(max_length=15, verbose_name='Especifique su certificación')),
                ('herr_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Moodle'), ('2', 'Microsoft Teams'), ('3', 'Zoom'), ('4', 'Google Classroom'), ('5', 'Otros')], default='', max_length=1, verbose_name='¿Qué herramientas tecnológicas utilizas en tus clases?')),
                ('herr_esp_inf_pro', models.CharField(max_length=15, verbose_name='Especifique otra herramienta tecnológica')),
                ('comp_dig_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Sí'), ('2', 'No')], default='', max_length=1, verbose_name='¿Posees competencias digitales específicas (ej. DigCompEdu)?')),
                ('comp_dig_esp_inf_pro', models.CharField(max_length=15, verbose_name='Especifique cuales')),
                ('mod_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Presencial'), ('2', 'En línea'), ('3', 'Mixta')], default='', max_length=1, verbose_name='Qué modalidades de enseñanza prefieres impartir')),
                ('tipo_alu_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Jóvenes'), ('2', 'Adultos'), ('3', 'Empresas'), ('4', 'Otros')], default='', max_length=1, verbose_name='Qué tipo de alumnado prefieres formar')),
                ('tipo_alu_esp_inf_pro', models.CharField(max_length=15, verbose_name='Especifique el tipo de alumnos')),
                ('franja_inf_pro', models.CharField(choices=[('', 'Seleccione una opción'), ('1', 'Mañana (8:00-14:00)'), ('2', 'Tarde (14:00-20:00)'), ('3', 'Noche (20:00-23:00)')], default='', max_length=1, verbose_name='En qué franjas horarias estás disponible para impartir clases?')),
                ('fk_per_inf_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_alumnalia.dat_per', verbose_name='fk de Datos de personas')),
            ],
            options={
                'db_table': 'Inf_Prof',
            },
        ),
        migrations.CreateModel(
            name='Info_Estu',
            fields=[
                ('pk_inf_est', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='id de la Información Estudiante')),
                ('int_form_inf_est', models.CharField(max_length=15, verbose_name='intereses formativos')),
                ('que_que_est', models.CharField(max_length=15, verbose_name='qué querrían estudiar')),
                ('que_has_est', models.CharField(max_length=15, verbose_name=' qué han estudiado')),
                ('de_que_han_trab', models.CharField(max_length=15, verbose_name='de qué han trabajado')),
                ('de_que_que_trab', models.CharField(max_length=15, verbose_name='de qué querrían trabajar')),
                ('rang_sal_des', models.FloatField(max_length=2, verbose_name='rango salarial deseado')),
                ('cv_adj_inf_est', models.FileField(blank=True, null=True, upload_to='pdfs/', verbose_name='Adjunta tu currículum en formato PDF.')),
                ('fk_per_inf_est', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_alumnalia.dat_per', verbose_name='fk de Datos de personas')),
            ],
            options={
                'db_table': 'Info_Estu',
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('pk_mun', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de Municipios')),
                ('nom_mun', models.CharField(max_length=30, verbose_name='nombre de la Municipios')),
                ('fk_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Municipios', to='app_alumnalia.comarca')),
            ],
            options={
                'db_table': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Ent_For',
            fields=[
                ('pk_ent_for', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Entidad Formadora')),
                ('nom_ent_for', models.CharField(max_length=44, verbose_name='nombre de Entidad Formadora')),
                ('Area_for_ent_for', models.CharField(max_length=44, verbose_name='area de formacion de Entidad Formadora')),
                ('email_ent_for', models.EmailField(max_length=254, verbose_name='correo de la entidad')),
                ('nif_ent_for', models.CharField(max_length=20, verbose_name='NIF de Entidad Formadora')),
                ('fec_fin_ent_for', models.DateField(verbose_name='Fecha de fin')),
                ('fec_ini_ent_for', models.DateField(verbose_name='Fecha de inicio')),
                ('area_prof_ent_for', models.CharField(max_length=44, verbose_name='Area Porfecional de Entidad Formadora')),
                ('cm_ent_for', models.CharField(max_length=5, verbose_name='Codigo del municipio de Entidad Formadora')),
                ('web_ent_for', models.CharField(max_length=100, verbose_name='link de la web de Entidad Formadora')),
                ('horas_ent_for', models.IntegerField(verbose_name='horas de la Entidad Formadora')),
                ('idt_ent_for', models.IntegerField(verbose_name='identificador de la Entiad Formadora')),
                ('den_ent_for', models.CharField(max_length=100, verbose_name='Denominacion de Entidad Formadora')),
                ('amb_ent_for', models.CharField(max_length=100, verbose_name='Ambito de Entidad Formadora')),
                ('mod_ent_for', models.CharField(max_length=50, verbose_name='Modalidad de Entidad Formadora')),
                ('num_grupo', models.IntegerField(verbose_name='Numero de grupo de la Entidad Formadora')),
                ('telefono', models.CharField(max_length=15, validators=[app_alumnalia.modelos.modelFormacion.validar_longitud_nueve], verbose_name='telefono de Entidad Formadora')),
                ('fk_com_ent_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comarca', to='app_alumnalia.comarca')),
                ('fk_fam_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Familia_Profesion', to='app_alumnalia.familia_profesion')),
                ('fk_mun_ent_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Municipios', to='app_alumnalia.municipios')),
            ],
            options={
                'db_table': 'Ent_For',
            },
        ),
        migrations.AddField(
            model_name='dat_per',
            name='fk_mun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_alumnalia.municipios', verbose_name='Municipio'),
        ),
        migrations.CreateModel(
            name='Oferta_Formativa',
            fields=[
                ('pk_Ofe_for', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id de Oferta Formadora')),
                ('nom_ofe', models.CharField(max_length=44, verbose_name='nombre de la oferta')),
                ('Area_for_ent_for', models.CharField(max_length=44, verbose_name='Area de formacion de la oferta')),
                ('fk_cal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Escuela', to='app_alumnalia.calendario')),
                ('fk_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Escuela', to='app_alumnalia.comarca')),
                ('fk_cur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Escuela', to='app_alumnalia.cusrso')),
                ('fk_esc_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Escuela', to='app_alumnalia.escuela')),
                ('fk_mun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Escuela', to='app_alumnalia.municipios')),
                ('fk_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Escuela', to='app_alumnalia.provincias')),
            ],
            options={
                'db_table': 'Oferta_Formativa',
            },
        ),
        migrations.AddField(
            model_name='dat_per',
            name='fk_pro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_alumnalia.provincias', verbose_name='Provincia'),
        ),
        migrations.CreateModel(
            name='Comarca_provincias',
            fields=[
                ('pk_cam_pro', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='id de Comarca_provincias')),
                ('fk_com', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comarca_provincias', to='app_alumnalia.comarca', verbose_name='id de la Comarca')),
                ('fk_pro', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comarca_provincias', to='app_alumnalia.provincias', verbose_name='id de la Provicia')),
            ],
            options={
                'db_table': 'Comarca_provincias',
            },
        ),
        migrations.AddField(
            model_name='dat_per',
            name='fk_via',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_alumnalia.tipovia', verbose_name='Tipo de via'),
        ),
    ]
