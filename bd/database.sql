

create table users(
    id int primary key,
    password varchar(25),
    nombre varchar(24)
),
create table modulo(
    id int primary key,
    hora_ini varchar(25),
    hora_fin varchar(25)
),
create table asistentes(
    id int primary key,
    nombre varchar(30)
),
create table clase(
    id int primary key,
    nombre_clase varchar(29)
),
create table horario(
    id_modulo int,
    id_asistente int,
    id_clase int,
    primary key (id_modulo,id_asistente,id_clase),
    CONSTRAINT FK_modulo foreign key (id_modulo) references modulo(id),
    CONSTRAINT FK_asistente foreign key (id_asistente) references asistentes(id),
    CONSTRAINT FK_clase foreign key (id_clase) references clase(id)
); -- relacion triple (asistente - modulo - clase)
