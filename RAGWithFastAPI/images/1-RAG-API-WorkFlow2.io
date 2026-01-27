<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36" version="28.2.8">
  <diagram name="RAG API Flow (Corrected)" id="0">
    <mxGraphModel dx="2066" dy="1080" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="title" value="RAG API Workflow" style="text;html=1;align=center;verticalAlign=middle;fontSize=28;fontStyle=1" parent="1" vertex="1">
          <mxGeometry x="280" y="40" width="500" height="50" as="geometry" />
        </mxCell>
        <mxCell id="userAsk" value="👤 User&lt;br&gt;Ask Question" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" parent="1" vertex="1">
          <mxGeometry x="70" y="250" width="160" height="70" as="geometry" />
        </mxCell>
        <mxCell id="fastapi" value="FastAPI&lt;br&gt;API Server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" parent="1" vertex="1">
          <mxGeometry x="310" y="330" width="260" height="100" as="geometry" />
        </mxCell>
        <mxCell id="userResp" value="👤 User&lt;br&gt;Get Response" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" parent="1" vertex="1">
          <mxGeometry x="70" y="400" width="180" height="70" as="geometry" />
        </mxCell>
        <mxCell id="chroma" value="Chroma DB&lt;br&gt;Search Knowledge Base" style="shape=cylinder;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" parent="1" vertex="1">
          <mxGeometry x="420" y="140" width="260" height="110" as="geometry" />
        </mxCell>
        <mxCell id="ollama" value="Ollama LLM Server&lt;div&gt;(locally running)&lt;br&gt;&lt;br&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" parent="1" vertex="1">
          <mxGeometry x="720" y="360" width="240" height="70" as="geometry" />
        </mxCell>
        <mxCell id="e1" value="1" style="endArrow=block;html=1;labelBackgroundColor=#ffffff" parent="1" source="userAsk" target="fastapi" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" value="2" style="endArrow=block;html=1;labelBackgroundColor=#ffffff;entryX=0.094;entryY=0.894;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="fastapi" target="chroma" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" value="3" style="endArrow=block;html=1;labelBackgroundColor=#ffffff;entryX=0.75;entryY=0;entryDx=0;entryDy=0;" parent="1" source="chroma" target="fastapi" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="500" y="270" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e4" value="4" style="endArrow=block;html=1;labelBackgroundColor=#ffffff;exitX=1;exitY=0.25;exitDx=0;exitDy=0;" parent="1" source="fastapi" target="ollama" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" value="5" style="endArrow=block;html=1;labelBackgroundColor=#ffffff;entryX=1;entryY=0.75;entryDx=0;entryDy=0;" parent="1" source="ollama" target="fastapi" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e6" value="6" style="endArrow=block;html=1;labelBackgroundColor=#ffffff" parent="1" source="fastapi" target="userResp" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="pyXog-NQ1eqiJfeqZBr6-1" value="WorkFlow:&#xa;&#xa;1 User          Ask question (prompt) via FastAPI client endpoint (question)&#xa;2 FastAPI    Search Chroma DB KB for the context (retrieve context)&#xa;3 Chroma    Get the context info from Chorma DB to FastAPI (retrieved context docs)&#xa;4 FastAPI    Send prompt + context info to Ollama LLM (prompt + context)&#xa;5 Ollama      LLMA response back to FastAPI (generated answer)&#xa;6 FastAPI    Response back to the User (final response)" style="text;whiteSpace=wrap;fontSize=16;spacingTop=10;spacing=2;" parent="1" vertex="1">
          <mxGeometry x="90" y="520" width="610" height="190" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
