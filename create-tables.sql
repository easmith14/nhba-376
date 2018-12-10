CREATE DATABASE nhba;
USE nhba;

CREATE TABLE `Buildings` (
        `PK_building_id` VARCHAR(255)  NOT NULL,
        `building_name_common` VARCHAR(255)  NOT NULL,
        `building_name_historic` VARCHAR(255),
        `address` VARCHAR(255)  NOT NULL,
        `year_built` YEAR,
        `latitude` float,
        `longitude` float,
        `client` VARCHAR(255),

        `FK_current_uses` VARCHAR(255),
        `FK_current_tenant` VARCHAR(255),
        `FK_architect` VARCHAR(255),
        `FK_contractor` VARCHAR(255),
        `FK_researcher` VARCHAR(255),

        `historic_uses` VARCHAR(255),
        `past_tenants` VARCHAR(255),
        `styles` VARCHAR(255),
        `threats_to_site` VARCHAR(255),
        `neighborhoods` VARCHAR(255),
        `sources` TEXT,
        `tours` VARCHAR(255),
        `images` TEXT,
        `archive_documents` TEXT,
        `related_buildings_and_features` VARCHAR(255),

        `era` VARCHAR(255),
        `current_owner` VARCHAR(255),
        `visible_from_road` VARCHAR(255),
        `interior_accessible` VARCHAR(255),
        `date_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        `date_last_modified` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        `overview` LONGTEXT,
        `physical_description` LONGTEXT,
        `streetscape_urban_setting` LONGTEXT,
        `social_history` LONGTEXT,
        `site_history` LONGTEXT,
        `materials` VARCHAR(255),
        `structural_systems` VARCHAR(255),
        `roof` VARCHAR(255),
        `roof_materials` VARCHAR(255),
        `number_stories` VARCHAR(255),
        `structural_conditions` VARCHAR(255),
        `external_conditions` VARCHAR(255),
        `dimensions` VARCHAR(255),
        `alterations` TEXT,
        `creator` VARCHAR(255) NOT NULL,
        `draft` BOOLEAN,

        PRIMARY KEY (PK_building_id)
        -- FOREIGN KEY (FK_current_uses) REFERENCES Building_Usages(id)
        -- FOREIGN KEY (FK_current_tenant) REFERENCES Tenants(id),
        -- FOREIGN KEY (FK_architect) REFERENCES Architects(id),
        -- FOREIGN KEY (FK_contractor) REFERENCES Contractors(id),
        -- FOREIGN KEY (FK_researcher) REFERENCES Researchers(FK_id)
);

CREATE TABLE `Tours` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(255)  NOT NULL,
    `date_created` DATE NOT NULL,
    `date_modified` DATE NOT NULL,
    `order` VARCHAR(255),
    `status`  VARCHAR(255),
    `comment_count` VARCHAR(255),
    `creator` VARCHAR(255),

    PRIMARY KEY (id)
);

CREATE TABLE `Users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255)  NOT NULL,
    `last_name`  VARCHAR(255)  NOT NULL,
    `email` VARCHAR(255)  NOT NULL,
    `validated` BOOLEAN,
    `admin` BOOLEAN,
    `superadmin` BOOLEAN,
    `contributor` BOOLEAN,

    PRIMARY KEY (id)
);

CREATE TABLE `Researchers` (
    `FK_id` INT NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255)  NOT NULL,
    `last_name`  VARCHAR(255)  NOT NULL,
    `num_active_posts` INT,
    `FK_draft_posts` VARCHAR(255),
    `num_posts`  INT,
    `FK_published_posts` VARCHAR(255),

    PRIMARY KEY (id),
    FOREIGN KEY (FK_id) REFERENCES Users(id)

);

CREATE TABLE `Tenants` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255)  NOT NULL,
    `last_name`  VARCHAR(255)  NOT NULL,
    `start_date`  DATE,
    `end_date` DATE,
    `current_tenant` BOOLEAN,

    PRIMARY KEY (id)
);

CREATE TABLE `Owners` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255)  NOT NULL,
    `last_name`  VARCHAR(255)  NOT NULL,
    `FK_type` INT NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (FK_type) REFERENCES Owner_Types(id)
);

CREATE TABLE `Architects` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255)  NOT NULL,
    `last_name`  VARCHAR(255)  NOT NULL,
    `firm` VARCHAR(255),

    PRIMARY KEY (id)
);

CREATE TABLE `Neighborhoods` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255)  NOT NULL,
    `alternate_names`  VARCHAR(255)  NOT NULL,

    PRIMARY KEY (id)
);

INSERT INTO `Neighborhoods` VALUES (
    (0, `Fair Haven`),
    (1, `Fair Haven Heights`),
    (2, `Mill River District`),
    (3, `Wooster Square`),
    (4, `Downtown and Town Green District`),
    (5, `Broadway`),
    (6, `Whitney-Audubon`),
    (7, `Chapel West`),
    (8, `Oak Street Connector`),
    (9, `Whalley-Edgewood-Dwight`),
    (10, `Upper State Street (closer to East Rock)`),
    (11, `Lower State Street (closer to Downtown)`),
    (12, `Ninth Square`),
    (13, `Westville`),
    (14, `Beaver Hill`),
    (15, `Newhallville`),
    (16, `East Rock`),
    (17, `West River`),
    (18, `Yale Campus`)
);

CREATE TABLE `Building_Usages` (
        `id` INT  NOT NULL   AUTO_INCREMENT,
        `usage` VARCHAR(255)  NOT NULL,

        PRIMARY KEY (id)
);

INSERT INTO `Building_Usages` VALUES (
    (0, `residential_single_family`),
    (1, `residential_two_family`),
    (2, `residential_rowhouse`),
    (3, `residential_multi_unit`),
    (4, `residential_outbuilding`),
    (5, `residential_vacant`),
    (6, `residential_other`),

    (7, `commercial_retail`),
    (8, `commercial_personal_care`),
    (9, `commercial_bank`),
    (10, `commercial_business_activities`),
    (11, `commercial_grocery`),
    (12, `commercial_bakery`),
    (13, `commercial_coffee`),
    (14, `commercial_restaurant`),
    (15, `commercial_bar`),
    (16, `commercial_theater`),
    (17, `commercial_auto`),
    (18, `commercial_furniture`),
    (19, `commercial_medical`),
    (20, `commercial_vacant`),
    (21, `commercial_other`),
    (22, `commercial_services`),

    (23, `industrial_warehouse`),
    (24, `industrial_commercial_bakery`),
    (25, `industrial_food_production`),
    (26, `industrial_waste_management`),
    (27, `industrial_mining`),
    (28, `industrial_art`),
    (29, `industrial_utilities`),
    (30, `industrial_vacant`),
    (31, `industrial_other`),
    (32, `industrial_manufacturing`),

    (33, `institutional_university`),
    (34, `institutional_school`),
    (35, `institutional_firehouse`),
    (36, `institutional_post_office`),
    (37, `institutional_police`),
    (38, `institutional_courthouse`),
    (39, `institutional_hospital`),
    (40, `institutional_worship`),
    (41, `institutional_non_profit`),
    (42, `institutional_government`),

    (43, `infrastructure_monument`),
    (44, `infrastructure_park`),
    (45, `infrastructure_street`),
    (46, `infrastructure_public_art`),
    (47, `infrastructure_transport`),
    (48, `infrastructure_bridge`)
);

CREATE TABLE `Owner_Types` (
        `id` INT  NOT NULL   AUTO_INCREMENT,
        `type` VARCHAR(255)  NOT NULL,

        PRIMARY KEY (id)
);

INSERT INTO `Owner_Types` VALUES (
    (0, `Public`),
    (1, `Private`),
    (2, `Non-Profit`),
    (3, `City of New Haven`),
    (4, `Yale`)
);

CREATE TABLE `Eras` (
        `id` INT  NOT NULL   AUTO_INCREMENT,
        `era` VARCHAR(255)  NOT NULL,

        PRIMARY KEY (id)
);

INSERT INTO `Eras` VALUES (
    (0, `1638 - 1860`),
    (1, `1860 - 1910`),
    (2, `1910 - 1950`),
    (3, `1950 - 1980`),
    (4, `1980 - today`)
);

CREATE TABLE `Materials` (
        `id` INT  NOT NULL   AUTO_INCREMENT,
        `type` VARCHAR(255)  NOT NULL,

        PRIMARY KEY (id)
);

INSERT INTO `Materials` VALUES (
    (0, `Clapboard`),
    (1, `Asbestos Siding`),
    (2, `Brick`),
    (3, `Wood Shingle`),
    (4, `Asphalt Siding`),
    (5, `Fieldstone`),
    (6, `Board & Batten`),
    (7, `Stucco`),
    (8, `Cobblestone`),
    (9, `Aluminum Siding`),
    (10, `Poured Concrete`),
    (11, `Precast Concrete`),
    (12, `Concrete block`),
    (13, `Cut stone`)
);

CREATE TABLE `Structural_Systems` (
        `id` INT  NOT NULL   AUTO_INCREMENT,
        `type` VARCHAR(255)  NOT NULL,

        PRIMARY KEY (id)
);

INSERT INTO `Structural_Systems` VALUES (
    (0, `Heavy Timbers`),
    (1, `Balloon Framing`),
    (2, `Platform Framing`),
    (3, `Load-bearing masonry`),
    (4, `Poured or pre-cast concrete`),
    (5, `Structural iron or steel`),
    (6, `Add Selection`)
);

CREATE TABLE `Roof_Types` (
        `id` INT  NOT NULL   AUTO_INCREMENT,
        `type` VARCHAR(255)  NOT NULL,

        PRIMARY KEY (id)
);

INSERT INTO `Roof_Types` VALUES (
    (0, `Gable`),
    (1, `Flat`),
    (2, `Mansard`),
    (3, `Monitor`),
    (4, `Sawtooth`),
    (5, `Gambrel`),
    (6, `Shed`),
    (7, `Hip`),
    (8, `Round`),
    (9, `Add Selection`)
);

CREATE TABLE `Roof_Materials` (
        `id` INT  NOT NULL   AUTO_INCREMENT,
        `type` VARCHAR(255)  NOT NULL,

        PRIMARY KEY (id)
);

INSERT INTO `Roof_Materials` VALUES (
    (0, `Wood Shingle`),
    (1, `Roll Asphalt`),
    (2, `Tin`),
    (3, `Slate`),
    (4, `Asphalt shingle`),
    (5, `Tile`),
    (6, `Add Selection`)
);


CREATE TABLE `Related_Buildings` (
    `id` INT  NOT NULL   AUTO_INCREMENT,
    `type` VARCHAR(255)  NOT NULL,

    PRIMARY KEY (id)
);

INSERT INTO `Related_Buildings` VALUES (
    (0, `Barn`),
    (1, `Shed`),
    (2, `Garage`),
    (3, `Carriage House`),
    (4, `Shop`),
    (5, `Garden`),
    (6, `Add Selection`)
);

CREATE TABLE `Threats` (
    `id` INT  NOT NULL   AUTO_INCREMENT,
    `type` VARCHAR(255)  NOT NULL,

    PRIMARY KEY (id)
);

INSERT INTO `Threats` VALUES (
    (0, `None known`),
    (1, `Road-building`),
    (2, `Vandalism`),
    (3, `Development`),
    (4, `Neglect / Deterioration`),
    (5, `Add Selection`)
);
