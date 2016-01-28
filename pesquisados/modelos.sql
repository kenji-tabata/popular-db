-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u2
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tempo de Geração: 28/01/2016 às 13:15:09
-- Versão do Servidor: 5.5.46
-- Versão do PHP: 5.6.16-1~dotdeb+7.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de Dados: `cli_sdd_testes`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `pesq_comple`
--

CREATE TABLE IF NOT EXISTS `pesq_comple` (
  `id_pesq` int(11) NOT NULL,
  `dt_nasc` date NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `bairro` varchar(50) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `uf` varchar(2) NOT NULL,
  `cep` varchar(10) NOT NULL,
  `telefone_res` varchar(20) NOT NULL,
  `telefone_cel` varchar(20) NOT NULL,
  `telefone_com` varchar(20) NOT NULL,
  `email` varchar(150) NOT NULL,
  `formacao` varchar(50) NOT NULL,
  `empresa` varchar(50) NOT NULL,
  `dt_adm` varchar(30) NOT NULL,
  `dt_preen` date NOT NULL,
  UNIQUE KEY `id_pesq` (`id_pesq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pesq_main`
--

CREATE TABLE IF NOT EXISTS `pesq_main` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_grupo` int(11) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `oculto` tinyint(1) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `cpf` varchar(15) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pesq_perf`
--

CREATE TABLE IF NOT EXISTS `pesq_perf` (
  `id_pesq` int(11) NOT NULL,
  `id_perf` int(11) DEFAULT NULL,
  `base` varchar(9) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  `empr` int(11) DEFAULT NULL,
  `com` int(11) DEFAULT NULL,
  `arg` int(11) DEFAULT NULL,
  `vel` int(11) DEFAULT NULL,
  `prat` int(11) DEFAULT NULL,
  `det` int(11) DEFAULT NULL,
  `orga` int(11) DEFAULT NULL,
  `cnor` int(11) DEFAULT NULL,
  `perc` int(11) DEFAULT NULL,
  `intu` int(11) DEFAULT NULL,
  `crit` int(11) DEFAULT NULL,
  `decir` int(11) DEFAULT NULL,
  `cria` int(11) DEFAULT NULL,
  `ener` int(11) DEFAULT NULL,
  `alternativas` text NOT NULL,
  `el` text,
  `sit` text,
  UNIQUE KEY `id_pesq` (`id_pesq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Restrições para as tabelas dumpadas
--

--
-- Restrições para a tabela `pesq_comple`
--
ALTER TABLE `pesq_comple`
  ADD CONSTRAINT `pesq_comple_ibfk_1` FOREIGN KEY (`id_pesq`) REFERENCES `pesq_main` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para a tabela `pesq_perf`
--
ALTER TABLE `pesq_perf`
  ADD CONSTRAINT `pesq_perf_ibfk_1` FOREIGN KEY (`id_pesq`) REFERENCES `pesq_main` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;