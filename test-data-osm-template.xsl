<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/osm">
    <osmChange version="0.6">
      <modify>
	<xsl:copy-of select="/osm/*"/>
      </modify>
    </osmChange>
  </xsl:template>

</xsl:stylesheet>
