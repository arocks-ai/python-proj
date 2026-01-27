<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36" version="28.2.8" pages="2">
  <diagram name="RAG API Flow" id="0">
    <mxGraphModel dx="2066" dy="1080" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="title" value="How RAG API Works" style="text;html=1;align=center;verticalAlign=middle;fontSize=28;fontStyle=1" parent="1" vertex="1">
          <mxGeometry x="350" y="20" width="500" height="50" as="geometry" />
        </mxCell>
        <mxCell id="userAsk" value="👤 You&#xa;Ask Question" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#000000" parent="1" vertex="1">
          <mxGeometry x="60" y="260" width="160" height="70" as="geometry" />
        </mxCell>
        <mxCell id="fastapi" value="FastAPI&#xa;Your API Server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#2f2f2f;fontColor=#ffffff;strokeColor=#000000" parent="1" vertex="1">
          <mxGeometry x="310" y="300" width="200" height="70" as="geometry" />
        </mxCell>
        <mxCell id="userResp" value="👤 You&#xa;Get Response" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#000000" parent="1" vertex="1">
          <mxGeometry x="60" y="390" width="170" height="60" as="geometry" />
        </mxCell>
        <mxCell id="chroma" value="Chroma&#xa;Search Knowledge Base" style="shape=cylinder;whiteSpace=wrap;html=1;fillColor=#eaeaea;strokeColor=#000000" parent="1" vertex="1">
          <mxGeometry x="500" y="150" width="260" height="100" as="geometry" />
        </mxCell>
        <mxCell id="ollama" value="Ollama&#xa;AI Generates Answer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#2f2f2f;fontColor=#ffffff;strokeColor=#000000" parent="1" vertex="1">
          <mxGeometry x="760" y="300" width="220" height="70" as="geometry" />
        </mxCell>
        <mxCell id="e1" style="endArrow=block;html=1" parent="1" source="userAsk" target="fastapi" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" style="endArrow=block;html=1;exitX=-0.007;exitY=0.88;exitDx=0;exitDy=0;exitPerimeter=0;" parent="1" source="fastapi" target="userResp" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" style="endArrow=block;html=1" parent="1" source="fastapi" target="chroma" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" style="endArrow=block;html=1;exitX=0.85;exitY=0.95;exitDx=0;exitDy=0;exitPerimeter=0;" parent="1" source="chroma" target="ollama" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" style="endArrow=block;html=1" parent="1" source="ollama" target="fastapi" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
  <diagram id="PbiEYMqjl3hBIVrZp_Jd" name="Page-2">
    <mxGraphModel dx="2066" dy="1080" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
