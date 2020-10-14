/****** Object:  Table [dbo].[tbl_user]    Script Date: 10/13/2020 6:46:05 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[tbl_user]') AND type in (N'U'))
DROP TABLE [dbo].[tbl_user]
GO

/****** Object:  Table [dbo].[tbl_user]    Script Date: 10/13/2020 6:46:05 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tbl_user](
	[user_name] [nchar](100) NULL,
	[user_email] [nchar](100) NULL,
	[user_password] [nchar](100) NULL,
	[user_id] [nchar](100) NULL
) ON [PRIMARY]
GO

TRUNCATE TABLE tbl_user