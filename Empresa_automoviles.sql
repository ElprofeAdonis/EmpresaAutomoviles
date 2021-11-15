-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 02-11-2021 a las 00:03:27
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Empresa_automoviles`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `clien_CedulaIdentidad` int(34) NOT NULL,
  `clien_TipoCedulaIdentidad` enum('Cedula de identidad ( TSE)','DIMEX(Extranjero Residente)','NITE (Tributacion)','Cedula Juridica','Cedula Fisica') NOT NULL,
  `clien_PrimerNombre` varchar(150) NOT NULL,
  `clien_PrimerApellido` varchar(150) NOT NULL,
  `clien_CalificacionCrdito` int(100) NOT NULL,
  `clien_DireccionResidencia` varchar(150) NOT NULL,
  `clien_NumeroTelefono` int(150) NOT NULL,
  `clien_FechaNacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `clien_CedulaIdentidad`, `clien_TipoCedulaIdentidad`, `clien_PrimerNombre`, `clien_PrimerApellido`, `clien_CalificacionCrdito`, `clien_DireccionResidencia`, `clien_NumeroTelefono`, `clien_FechaNacimiento`) VALUES
(1, 504560789, 'Cedula de identidad ( TSE)', 'Pedro', 'Judas', 89, '400 metro norte del antiguo hospital que esta por mi casa', 68987463, '2021-03-09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

CREATE TABLE `vendedor` (
  `id` int(200) NOT NULL,
  `vend_CIV` int(10) NOT NULL,
  `vend_PrimerNombre` varchar(150) NOT NULL,
  `vend_PrimerApellido` varchar(150) NOT NULL,
  `vend_FechaNacimiento` date NOT NULL,
  `vend_Tipo` enum('Especialista en hatchback','Especialista en eVehiculo todo terreno','Especialista en sedan y SUUS','Especialista en camiones') NOT NULL,
  `vend_Salario` int(15) NOT NULL,
  `vend_DireccionResidencia` varchar(150) NOT NULL,
  `vend_NumeroTelefono` int(12) NOT NULL,
  `vend_PorcentajeComision` int(12) NOT NULL,
  `vend_MOntoComision` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `vendedor`
--

INSERT INTO `vendedor` (`id`, `vend_CIV`, `vend_PrimerNombre`, `vend_PrimerApellido`, `vend_FechaNacimiento`, `vend_Tipo`, `vend_Salario`, `vend_DireccionResidencia`, `vend_NumeroTelefono`, `vend_PorcentajeComision`, `vend_MOntoComision`) VALUES
(1, 2000045, 'Adonis', 'Gutierrez', '2021-06-08', 'Especialista en camiones', 4000, 'dedonte esta el palo demando bajando un toque mas', 1345637895, 4, 4000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `vent_CUV` int(11) NOT NULL,
  `vent_CodigoConsecutivo` int(25) NOT NULL,
  `vent_NumeroContrato` int(11) NOT NULL,
  `vent_CIV` int(11) NOT NULL,
  `vent_CedulaIdentidad` int(11) NOT NULL,
  `vent_Monto` int(11) NOT NULL,
  `vent_FechaVenta` date NOT NULL,
  `vent_Producto` varchar(3000) NOT NULL,
  `vent_Marca` varchar(3000) NOT NULL,
  `vent_Modelo` varchar(3000) NOT NULL,
  `vent_Anio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `vent_CUV`, `vent_CodigoConsecutivo`, `vent_NumeroContrato`, `vent_CIV`, `vent_CedulaIdentidad`, `vent_Monto`, `vent_FechaVenta`, `vent_Producto`, `vent_Marca`, `vent_Modelo`, `vent_Anio`) VALUES
(1, 1, 1, 8201, 2000045, 54567896, 5000, '2021-10-04', 'toyota corrolla 2020, hibrido, full extras, 4 puertas, asiento de cuero de lujo(extra), pack de halaogenos y parrilla, funcion de cargas rapida(Fastcharge Tecgh)', 'Toyota', 'sedan', 2020);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
